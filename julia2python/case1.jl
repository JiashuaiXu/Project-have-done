using OrdinaryDiffEq, Flux, Optim, Random, Plots
using Zygote
using ForwardDiff
using LinearAlgebra, Statistics
using ProgressBars, Printf
using Flux.Optimise: update!, ExpDecay
using Flux.Losses: mae, mse
using BSON: @save, @load
using Catalyst

Random.seed!(1234);

# TODO: use YAML file for configuration
# Argments
is_restart = false;
p_cutoff = 0.0;
n_epoch = 1000000;
n_plot = 100;
opt = ADAMW(0.0001, (0.9, 0.999), 0.0);
datasize = 100;
tstep = 0.1;
n_exp_train = 20;
n_exp_test = 10;
n_exp = n_exp_train + n_exp_test;
noise = 1.f-3;
ns = 5;
nr = 10;
k = [];
alg = Tsit5();
atol = 1e-5;
rtol = 1e-2;

maxiters = 10000;

lb = 1.f-5;

rn = @reaction_network begin
    (1.0, 1.0), A ↔ B
    (1.0, 1.0), B ↔ C
    (1.0, 1.0), C ↔ D
    # (1.0, 1.0), 2A ↔ B + C
    # (1.0, 1.0), 2B ↔ C + D
    (1.0, 1.0), 2C ↔ D + E
end

# Generate data sets
u0_list = rand(Float32, (n_exp, ns));
u0_list[:, 1:2] .+= 0.2;
# u0_list[:, 3:end] .= 0.0;
tspan = Float32[0.0, datasize * tstep];
tsteps = range(tspan[1], tspan[2], length=datasize);
ode_data_list = zeros(Float32, (n_exp, ns, datasize));
std_list = [];

function max_min(ode_data)
    return maximum(ode_data, dims=2) .- minimum(ode_data, dims=2) .+ lb
end

for i in 1:n_exp
    u0 = u0_list[i, :];
    prob_trueode = ODEProblem(rn, u0, tspan, k);
    ode_data = Array(solve(prob_trueode, alg, saveat=tsteps));
    ode_data += randn(size(ode_data)) .* ode_data .* noise
    ode_data_list[i, :, :] = ode_data
    push!(std_list, max_min(ode_data));
end
y_std = maximum(hcat(std_list...), dims=2);


p = randn(Float32, nr * (ns + 1)) .* 0.5;

function p2vec(p)
    w_kf = p[1:nr];
    w_kb = w_kf;  # assume Kc = 1
    w_out = reshape(p[nr + 1:end], ns, nr);
    w_out = clamp.(w_out, -2.5, 2.5)
    return w_kf, w_kb, w_out
end

function crnn!(du, u, p, t)
    w_in_f = clamp.(-w_out, 0, 2.5);
    w_in_b = clamp.(w_out, 0, 2.5);

    u_in = @. log(clamp(u, lb, Inf))
    w_in_x_f = w_in_f' * u_in;
    w_in_x_b = w_in_b' * u_in;
    
    du .= w_out * @. (exp(w_in_x_f + w_kf) - exp(w_in_x_b + w_kb));
end

u0 = u0_list[1, :]
prob = ODEProblem(crnn!, u0, tspan, saveat=tsteps,
                  atol=atol, rtol=rtol)

function pred_ode(u0, p)
    global w_kf, w_kb, w_out
    w_kf, w_kb, w_out = p2vec(p)
    pred = Array(solve(prob, alg, u0=u0, p=p; maxiters=maxiters))
    return pred
end
pred_ode(u0, p);
