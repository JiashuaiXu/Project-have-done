$(window).load(function() {
    $(".loading").fadeOut()
});
$(function() {
    i();
    j();
    k();
    l();
    m();
    n();
    o();
    p();

    function i() {
        var a = echarts.init(document.getElementById("echart1"));
        option = {
            tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)"
            },
            legend: {
                right: 0,
                top: 30,
                height: 160,
                itemWidth: 10,
                itemHeight: 10,
                itemGap: 10,
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: 12
                },
                orient: "vertical",
                data: ["营业收入", "利息收入", "已赚保费", "佣金收入", "业务收入"]
            },
            calculable: true,
            series: [{
                name: " ",
                color: ["#62c98d", "#2f89cf", "#4cb9cf", "#53b666", "#62c98d", "#205acf", "#c9c862", "#c98b62", "#c962b9", "#7562c9", "#c96262", "#c25775", "#00b7be"],
                type: "pie",
                radius: [30, 70],
                center: ["35%", "50%"],
                roseType: "radius",
                label: {
                    normal: {
                        show: true
                    },
                    emphasis: {
                        show: true
                    }
                },
                lableLine: {
                    normal: {
                        show: true
                    },
                    emphasis: {
                        show: true
                    }
                },
                data: [{
                    value: 10,
                    name: "流动资产"
                }, {
                    value: 5,
                    name: "货币资金"
                }, {
                    value: 15,
                    name: "结算备付金"
                }, {
                    value: 25,
                    name: "交易性金融资产"
                }, {
                    value: 20,
                    name: "衍生金融资产"
                }, ]
            }, ]
        };
        a.setOption(option);
        window.addEventListener("resize", function() {
            a.resize()
        })
        a.on('click', function() {
            window.open("https://gitee.com/iGaoWei/big-data-view");
        });
    }

    function j() {
        var a = echarts.init(document.getElementById("echart2"));
        option = {
            tooltip: {
                trigger: "item",
                formatter: "{b} : {c} ({d}%)"
            },
            legend: {
                top: "15%",
                data: ["图例1", "图例2", "图例3", "图例4", "图例5"],
                icon: "circle",
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                }
            },
            calculable: true,
            series: [{
                name: "",
                color: ["#62c98d", "#2f89cf", "#4cb9cf", "#53b666", "#62c98d", "#205acf", "#c9c862", "#c98b62", "#c962b9", "#c96262"],
                type: "pie",
                startAngle: 0,
                radius: [51, 100],
                center: ["50%", "45%"],
                roseType: "area",
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: true,
                    },
                    emphasis: {
                        show: true
                    }
                },
                labelLine: {
                    normal: {
                        show: true,
                        length2: 1,
                    },
                    emphasis: {
                        show: true
                    }
                },
                data: [{
                    value: 1,
                    name: "买入",
                }, {
                    value: 4,
                    name: "卖出",
                }, {
                    value: 5,
                    name: "最高",
                }, {
                    value: 6,
                    name: "最低",
                }, {
                    value: 9,
                    name: "昨收",
                }, {
                    value: 0,
                    name: "",
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                }, {
                    value: 0,
                    name: "",
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                }, {
                    value: 0,
                    name: "",
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                }, {
                    value: 0,
                    name: "",
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                }, {
                    value: 0,
                    name: "",
                    label: {
                        show: false
                    },
                    labelLine: {
                        show: false
                    }
                }, ]
            }]
        };
        a.setOption(option);
        window.addEventListener("resize", function() {
            a.resize()
        })
        a.on('click', function() {
            window.open("https://gitee.com/iGaoWei/big-data-view");
        });
    }

    function k() {
        var a = echarts.init(document.getElementById("echart3"));
        option = {
            tooltip: {
                trigger: "axis",
                axisPointer: {
                    lineStyle: {
                        color: "#57617B"
                    }
                }
            },
            legend: {
                data: ["销售额", "利润"],
                top: "0",
                textStyle: {
                    color: "#fff"
                },
                itemGap: 20,
            },
            grid: {
                left: "0",
                right: "20",
                top: "10",
                bottom: "20",
                containLabel: true
            },
            xAxis: [{
                type: "category",
                boundaryGap: false,
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)"
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }
                },
                data: ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
            }, {}],
            yAxis: [{
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)"
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }
                }
            }],
            series: [{
                name: "销售额",
                type: "line",
                smooth: true,
                symbol: "circle",
                symbolSize: 5,
                showSymbol: false,
                lineStyle: {
                    normal: {
                        width: 2
                    }
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: "rgba(24, 163, 64, 0.3)"
                        }, {
                            offset: 0.8,
                            color: "rgba(24, 163, 64, 0)"
                        }], false),
                        shadowColor: "rgba(0, 0, 0, 0.1)",
                        shadowBlur: 10
                    }
                },
                itemStyle: {
                    normal: {
                        color: "#00FF00",
                        borderColor: "rgba(137,189,2,0.27)",
                        borderWidth: 12
                    }
                },
                data: [220, 182, 191, 134, 150, 120, 110, 125, 145, 122, 165, 122]
            }, {
                name: "利润",
                type: "line",
                smooth: true,
                symbol: "circle",
                symbolSize: 5,
                showSymbol: false,
                lineStyle: {
                    normal: {
                        width: 2
                    }
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: "rgba(39, 122,206, 0.3)"
                        }, {
                            offset: 0.8,
                            color: "rgba(39, 122,206, 0)"
                        }], false),
                        shadowColor: "rgba(0, 0, 0, 0.1)",
                        shadowBlur: 10
                    }
                },
                itemStyle: {
                    normal: {
                        color: "#ff0000",
                        borderColor: "rgba(0,136,212,0.2)",
                        borderWidth: 12
                    }
                },
                data: [120, 110, 125, 145, 122, 165, 122, 220, 182, 191, 134, 150]
            }]
        };
        a.setOption(option);
        window.addEventListener("resize", function() {
            a.resize()
        })
        a.on('click', function() {
            window.open("https://gitee.com/iGaoWei/big-data-view");
        });
    }

    function l() {
        var a = echarts.init(document.getElementById("echart4"));
        option = {
            tooltip: {
                trigger: "axis",
                axisPointer: {
                    lineStyle: {
                        color: "#57617B"
                    }
                }
            },
            legend: {
                data: [{
                    name: "跌涨幅"
                }, {
                    name: "交易量"
                }, {
                    name: "完成率"
                }],
                top: "0%",
                textStyle: {
                    color: "rgba(255,255,255,0.9)"
                }
            },
            xAxis: [{
                type: "category",
                data: ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: "14",
                    },
                },
            }, ],
            yAxis: [{
                type: "value",
                name: "金额",
                min: 0,
                max: 50,
                interval: 10,
                axisLabel: {
                    show: true,
                },
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.4)"
                    }
                },
            }, {
                type: "value",
                name: "完成率",
                show: true,
                axisLabel: {
                    show: true,
                },
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.4)"
                    }
                },
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: "#001e94"
                    }
                },
            }, ],
            grid: {
                top: "10%",
                right: "30",
                bottom: "30",
                left: "30",
            },
            series: [{
                name: "买入",
                type: "bar",
                data: [4, 6, 36, 6, 8, 6, 4, 6, 30, 6, 8, 12],
                barWidth: "auto",
                itemStyle: {
                    normal: {
                        color: {
                            type: "linear",
                            x: 0,
                            y: 0,
                            x2: 0,
                            y2: 1,
                            colorStops: [{
                                offset: 0,
                                color: "#609db8"
                            }, {
                                offset: 1,
                                color: "#609db8"
                            }],
                            globalCoord: false
                        }
                    }
                }
            }, {
                name: "卖出",
                type: "bar",
                data: [4, 2, 34, 6, 8, 6, 4, 2, 32, 6, 8, 18],
                barWidth: "auto",
                itemStyle: {
                    normal: {
                        color: {
                            type: "linear",
                            x: 0,
                            y: 0,
                            x2: 0,
                            y2: 1,
                            colorStops: [{
                                offset: 0,
                                color: "#66b8a7"
                            }, {
                                offset: 1,
                                color: "#66b8a7"
                            }],
                            globalCoord: false
                        }
                    }
                },
                barGap: "0"
            }, {
                name: "完成率",
                type: "line",
                yAxisIndex: 1,
                data: [100, 50, 80, 30, 90, 40, 70, 33, 100, 40, 80, 20],
                lineStyle: {
                    normal: {
                        width: 2
                    },
                },
                itemStyle: {
                    normal: {
                        color: "#cdba00",
                    }
                },
                smooth: true
            }]
        };
        a.setOption(option);
        window.addEventListener("resize", function() {
            a.resize()
        })
        a.on('click', function() {
            alert("联系我qq:s1035377039");
        });
    }

    function m() {
        var b = echarts.init(document.getElementById("echart5"));
        var a = {
            type: "linear",
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [{
                offset: 0,
                color: "rgba(41, 121, 255, 1)"
            }, {
                offset: 1,
                color: "rgba(0, 192, 255, 1)"
            }],
            globalCoord: false
        };
        var c = {
            tooltip: {
                show: false
            },
            grid: {
                top: "0%",
                left: "65",
                right: "14%",
                bottom: "0%",
            },
            xAxis: {
                min: 0,
                max: 100,
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: false
                },
                axisLabel: {
                    show: false
                }
            },
            yAxis: {
                data: ["星昊医药", "诺思兰德", "同辉信息", "华岭股份", "微创光电", "辰光医疗", "苏轴股份", "乐创技术", "海能技术", "峆一药业", "三态股份"],
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: false
                },
                axisLabel: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: 14
                }
            },
            series: [{
                type: "bar",
                label: {
                    show: true,
                    zlevel: 10000,
                    position: "right",
                    padding: 10,
                    color: "#49bcf7",
                    fontSize: 14,
                    formatter: "{c}%"
                },
                itemStyle: {
                    color: "#49bcf7"
                },
                barWidth: "15",
                data: [49, 80, 67, 99, 12, 19, 39, 84, 28, 47, 57, 100],
                z: 10
            }, {
                type: "bar",
                barGap: "-100%",
                itemStyle: {
                    color: "#fff",
                    opacity: 0.1
                },
                barWidth: "15",
                data: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
                z: 5
            }],
        };
        b.setOption(c);
        window.addEventListener("resize", function() {
            b.resize()
        })
    }

    function n() {
        var a = echarts.init(document.getElementById("zb1"));
        var b = 298;
        var c = 523;
        var d = b + c;
        option = {
            series: [{
                type: "pie",
                radius: ["60%", "70%"],
                color: "#49bcf7",
                label: {
                    normal: {
                        position: "center"
                    }
                },
                data: [{
                    value: c,
                    name: "女消费",
                    label: {
                        normal: {
                            formatter: c + "",
                            textStyle: {
                                fontSize: 20,
                                color: "#fff",
                            }
                        }
                    }
                }, {
                    value: b,
                    name: "男消费",
                    label: {
                        normal: {
                            formatter: function(e) {
                                return "占比" + Math.round(c / d * 100) + "%"
                            },
                            textStyle: {
                                color: "#aaa",
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: "rgba(255,255,255,.2)"
                        },
                        emphasis: {
                            color: "#fff"
                        }
                    },
                }]
            }]
        };
        a.setOption(option);
        window.addEventListener("resize", function() {
            a.resize()
        })
        a.on('click', function() {
            alert("哈哈");
        });
    }

    function o() {
        var a = echarts.init(document.getElementById("zb2"));
        var b = 298;
        var c = 523;
        var d = b + c;
        option = {
            series: [{
                type: "pie",
                radius: ["60%", "70%"],
                color: "#cdba00",
                label: {
                    normal: {
                        position: "center"
                    }
                },
                data: [{
                    value: b,
                    name: "男消费",
                    label: {
                        normal: {
                            formatter: b + "",
                            textStyle: {
                                fontSize: 20,
                                color: "#fff",
                            }
                        }
                    }
                }, {
                    value: c,
                    name: "女消费",
                    label: {
                        normal: {
                            formatter: function(e) {
                                return "占比" + Math.round(b / d * 100) + "%"
                            },
                            textStyle: {
                                color: "#aaa",
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: "rgba(255,255,255,.2)"
                        },
                        emphasis: {
                            color: "#fff"
                        }
                    },
                }]
            }]
        };
        a.setOption(option);
        window.addEventListener("resize", function() {
            a.resize()
        })
    }

    function p() {
        var a = echarts.init(document.getElementById("zb3"));
        var b = 298;
        var c = 523;
        var d = b + c;
        option = {
            series: [{
                type: "pie",
                radius: ["60%", "70%"],
                color: "#62c98d",
                label: {
                    normal: {
                        position: "center"
                    }
                },
                data: [{
                    value: c,
                    name: "现金   消费",
                    label: {
                        normal: {
                            formatter: c + "",
                            textStyle: {
                                fontSize: 20,
                                color: "#fff",
                            }
                        }
                    }
                }, {
                    value: b,
                    name: "消费",
                    label: {
                        normal: {
                            formatter: function(e) {
                                return "占比" + Math.round(c / d * 100) + "%"
                            },
                            textStyle: {
                                color: "#aaa",
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: "rgba(255,255,255,.2)"
                        },
                        emphasis: {
                            color: "#fff"
                        }
                    },
                }]
            }]
        };
        a.setOption(option);
        window.addEventListener("resize", function() {
            a.resize()
        })
        a.on('click', function() {
            alert("联系我");
        });
    }
});