/* jshint quotmark: false */
/* global d3, _ */
'use strict';

(function() {

    var duration = 4900;
    var bisectDate = d3.bisector(function(d) { return d.time; }).left;
    var duration = 1000;

    function classOfChange(group, value) {
        console.log("Value : " + value);
        if (group === "solar") {
            return value < 0 ? "red" : "green";
        }
        return value > 0 ? "red" : "green";
    }

    function arrowUp(g, cls) {
        return g.append("path")
            .attr("d", "M52,84V21.656l21.457,21.456c1.561,1.562,4.095,1.562,5.656,0.001c1.562-1.562,1.562-4.096,0-5.658L50.829,9.172l0,0  c-0.186-0.186-0.391-0.352-0.609-0.498c-0.101-0.067-0.21-0.114-0.315-0.172c-0.124-0.066-0.242-0.142-0.373-0.195  c-0.135-0.057-0.275-0.089-0.415-0.129c-0.111-0.033-0.216-0.076-0.331-0.099C48.527,8.027,48.264,8,48.001,8l0,0  c-0.003,0-0.006,0.001-0.009,0.001c-0.259,0.001-0.519,0.027-0.774,0.078c-0.12,0.024-0.231,0.069-0.349,0.104  c-0.133,0.039-0.268,0.069-0.397,0.123c-0.139,0.058-0.265,0.136-0.396,0.208c-0.098,0.054-0.198,0.097-0.292,0.159  c-0.221,0.146-0.427,0.314-0.614,0.501L16.889,37.456c-1.562,1.562-1.562,4.095-0.001,5.657c1.562,1.562,4.094,1.562,5.658,0  L44,21.657V84c0,2.209,1.791,4,4,4S52,86.209,52,84z")
            .attr("class", "arrow up " + cls);
    }

    function arrowDown(g, cls) {
        return g.append("path")
            .attr("d", "M44,12v62.344L22.543,52.888c-1.561-1.562-4.094-1.562-5.656-0.001c-1.562,1.562-1.562,4.096,0,5.658l28.284,28.283l0,0  c0.186,0.186,0.391,0.352,0.609,0.498c0.101,0.067,0.21,0.114,0.315,0.172c0.124,0.066,0.242,0.142,0.373,0.195  c0.135,0.057,0.275,0.089,0.415,0.129c0.111,0.033,0.216,0.076,0.331,0.099C47.474,87.973,47.737,88,48,88l0,0  c0.003,0,0.006-0.001,0.009-0.001c0.259-0.001,0.519-0.027,0.774-0.078c0.12-0.024,0.231-0.069,0.348-0.104  c0.133-0.039,0.268-0.069,0.397-0.123c0.139-0.058,0.265-0.136,0.396-0.208c0.098-0.054,0.198-0.097,0.292-0.159  c0.221-0.146,0.427-0.314,0.614-0.501l28.281-28.282c1.562-1.562,1.562-4.095,0.001-5.657c-1.562-1.562-4.095-1.562-5.657,0  L52,74.343V12c0-2.209-1.791-4-4-4S44,9.791,44,12z")
            .attr("class", "arrow down " + cls);
    }

    function arrowOf(svg, group, value) {
        return (value < 0 ? arrowDown : arrowUp)(svg, classOfChange(group, value));
    }

    function updateData(originalData) {
        _.each(originalData, function(v, k) {
            v.this_month_money = v.charges.this_month;
            v.last_month_money = v.charges.last_month;
            v.last_year_money = v.charges.last_year;
            delete v.charges;
        });
        return originalData;
    }

    function fakeData(originalData) {
        _.each(originalData, function(data, k) {
            data.last_year = data.this_month + ( data.this_month / 20);
            data.last_month = data.this_month + ( data.this_month / 10);
            if (k === 'solar') {
                data.last_year = 0;
                data.last_month = data.this_month - ( data.this_month / 10);
            }
            if (k === 'demand') {
            } else {
                data.this_month *= 24;
                data.last_month *= 24;
                data.last_year *= 24;
            }
        });
        return originalData;
    }

    function plot(scope, el, data) {

        if (!data) {
            return;
        }

        data = updateData(data);
        data = fakeData(data);

        var total = {
            last_year: 0,
            last_month: 0,
            this_month: 0,
            this_month_money: 0,
            last_month_money: 0,
            last_year_money: 0
        };

        _.each(data, function(v, k) {
            if (k !== 'solar') {
                total.last_year += v.last_year;
                total.last_month += v.last_month;
                total.this_month += v.this_month;
                total.last_year_money += v.last_year_money;
                total.last_month_money += v.last_month_money;
                total.this_month_money += v.this_month_money;
            }
        });

        scope.yBegining = el[0].getBoundingClientRect().top;
        scope.margin = {top: 100, right: 0, bottom: 20, left: 40, between: 30};
        scope.width = el.width() - scope.margin.right - scope.margin.left;
        scope.height = el.height() - scope.margin.top - scope.margin.bottom;
        scope.bigheight = scope.height * 2 / 3;
        scope.smallheight = (scope.height / 3) - scope.margin.between;

        var maxValue = _(data).values().map(function(d) {
            return [d.last_year, d.last_month, d.this_month];
        }).flatten().max().value();

        maxValue += _.max([data.solar.last_month, data.solar.last_year, data.solar.this_month]);

        data.total = total;
        var maxTotalValue = _.max([
                data.total.last_month_money + data.solar.last_month_money,
                data.total.last_year_money + data.solar.last_year_money,
                data.total.this_month_money + data.solar.this_month_money]);
        
        var miniChartDomain = ['energy', 'demand', 'solar', 'total'];
        //var miniChartDomain = _.keys(data);
        scope.x = d3.scale.ordinal().rangeRoundBands([0, scope.width - scope.margin.left - scope.margin.right], .1);
        // To preserve the order
        scope.x.domain(miniChartDomain);

        scope.yTotal = d3.scale.linear().range([scope.bigheight, 0]);
        scope.y = d3.scale.linear().range([scope.bigheight, 0]);
        scope.y.domain([0, maxValue + 20]);
        scope.yTotal.domain([0, maxTotalValue + 20]);

        scope.svg = d3.select(el[0]).select(".graph").append("svg")
            .attr("width", scope.width + scope.margin.left + scope.margin.right)
            .attr("height", scope.height + scope.margin.top + scope.margin.bottom);

        var mainChart = scope.svg.append("g")
            .attr("class", "mainChart")
            .attr("transform", "translate(" + scope.margin.left + "," + scope.margin.top + ")");

        var miniChart = mainChart.selectAll("g") 
            // To preserve the order
            .data(miniChartDomain)
            .enter()
            .append("g")
            .attr("class", function(d) { return d; })
            .attr("transform", function(d) { return "translate(" + scope.x(d) + ",0)"; });

        var miniX = d3.scale.ordinal().rangeRoundBands([0, scope.x.rangeBand()], .3);

        miniChart.each(function(barsGroupName) {

            var chartData = data[barsGroupName];
            //var barsDomain = _.keys(chartData);
            var barsDomain = ['last_year', 'last_month', 'this_month'];
            miniX.domain(barsDomain);

            var chart = d3.select(this);

            var xLine = chart.select("line.x");
            if (xLine.empty()) {
                xLine = chart.append('line')
                    .attr("class", "x")
                    .attr("x1", 0)
                    .attr("x2", function(d) { return scope.x.rangeBand(); })
                    .attr("y1", scope.bigheight)
                    .attr("y2", scope.bigheight);
            }


            var big = chart.append("g")
                .attr("class", "big");

            var small = chart.append("g")
                .attr("class", "small")
                .attr("transform", "translate(0, " + ( scope.bigheight + scope.margin.between) + ")");

            var bar = chart.selectAll("g.barGroup")
                .data(barsDomain).enter()
                .append("g")
                .attr("class", function(d) { return "barGroup " + d; })
                .attr("transform", function(d) { return "translate(" + miniX(d) + ",0)"; });

            if (barsGroupName === 'total') {
                var solar = data.solar;
                var demand = data.demand;
                var energy = data.energy;

                bar.append("rect")
                    .attr("class", "energy")
                    .attr("y", scope.bigheight)
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var energy = scope.yTotal(data.energy[m] || 0);
                        return energy;
                    })
                    .attr("height", function(d) {
                        var m = d + '_money';
                        var energy = scope.yTotal(data.energy[m] || 0);
                        return scope.bigheight - energy;
                    });

                bar.append("text")
                    .attr("class", "energy_val")
                    .attr("x", miniX.rangeBand()/2)
                    .attr("y", scope.bigheight)
                    //.attr("height", function(d) { return scope.bigheight - scope.y(data.energy[d] || 0); })
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var energy = scope.yTotal(data.energy[m] || 0);
                        return energy + 15;
                    })
                    .text(function(d) { 
                        var val = Math.round(data.energy[d + '_money']);
                        if (!val) {
                            return '';
                        }
                        return val;
                    });

                bar.append("rect")
                    .attr("class", "demand")
                    .attr("y",  function(d) {
                        var m = d + '_money';
                        var energy = scope.yTotal(data.energy[m] || 0);
                        return energy;
                    })
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .delay(duration)
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var energy = scope.bigheight - scope.yTotal(data.energy[m] || 0);
                        var demand = scope.yTotal(data.demand[m] || 0);
                        var position = demand - energy;
                        return position;
                    })
                    .attr("height", function(d) {
                        var m = d + '_money';
                        var demand = scope.yTotal(data.demand[m] || 0);
                        return scope.bigheight - demand;
                    });

                bar.append("text")
                    .attr("class", "demand_val")
                    .attr("x", miniX.rangeBand()/2)
                    .attr("y",  function(d) {
                        var m = d + '_money';
                        var energy = scope.yTotal(data.energy[m] || 0);
                        return energy + 15;
                    })
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .delay(duration)
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var energy = scope.bigheight - scope.yTotal(data.energy[m] || 0);
                        var demand = scope.yTotal(data.demand[m] || 0);
                        var position = demand - energy;
                        return position + 15;
                    })
                    .text(function(d) {
                        var val =  Math.round(data.demand[d + '_money']);
                        if (!val) {
                            return '';
                        }
                        return val;
                    });


                bar.append("rect")
                    .attr("class", "solar")
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var demand = scope.bigheight - scope.yTotal(data.demand[m] || 0);
                        var energy = scope.yTotal(data.energy[m] || 0);
                        var position = energy - demand;
                        return position;
                    })
                    //.attr("height", function(d) { return scope.bigheight - scope.y(data.solar[d] || 0); })
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .delay(2 * duration)
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var solar = scope.bigheight - scope.yTotal(data.solar[m] || 0);
                        var demand = scope.bigheight - scope.yTotal(data.demand[m] || 0);
                        var energy = scope.bigheight - scope.yTotal(data.energy[m] || 0);
                        var position = scope.bigheight - solar - energy - demand;
                        return position;
                    })
                    .attr("height", function(d) { return scope.bigheight - scope.yTotal(data.solar[d + '_money'] || 0); });

                bar.append("text")
                    .attr("class", "solar_val")
                    .attr("x", miniX.rangeBand()/2)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var demand = scope.bigheight - scope.yTotal(data.demand[m] || 0);
                        var energy = scope.yTotal(data.energy[m] || 0);
                        var position = energy - demand;
                        return position;
                    })
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .delay(2 * duration)
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var solar = scope.bigheight - scope.yTotal(data.solar[m] || 0);
                        var demand = scope.bigheight - scope.yTotal(data.demand[m] || 0);
                        var energy = scope.bigheight - scope.yTotal(data.energy[m] || 0);
                        var position = scope.bigheight - solar - energy - demand;
                        return position + 15;
                    })
                    .text(function(d) {
                        var val =  Math.round(data.solar[d + '_money']);
                        if (!val) {
                            return '';
                        }
                        return "(" + val + ")";
                    });

            } else {
                bar.append("rect")
                    .attr("y", function(d) {
                        var height = scope.bigheight - scope.y(chartData[d] || 0);
                        var position = scope.y(chartData[d] || 0);
                        return height + position;
                    })
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .duration(duration)
                    .attr("y", function(d) {
                        var position = scope.y(chartData[d] || 0);
                        return position;
                    })
                    .attr("height", function(d) {
                        return scope.bigheight - scope.y(chartData[d] || 0);
                    });
            }

            // Bar value
            bar.append("text")
                .attr("x", miniX.rangeBand() / 2)
                .attr("y", function(d) { return scope.bigheight - 15; })
                .attr("dy", ".75em")
                .text(function(d) {
                    if (barsGroupName === 'total') {
                        var m = d + '_money';
                        var val = data.demand[m] + data.energy[m];
                        return '$ ' + Math.floor(val).toLocaleString();
                    }
                    return Math.round(chartData[d] || 0).toLocaleString();
                })
                .transition()
                .duration(duration)
                .attr("y", function(d) {
                    var position =  scope.y(chartData[d]) - 15;
                    if (barsGroupName === 'total') {
                        var m = d + '_money';
                        position = scope.yTotal(chartData[m] + data.solar[m]) - 15;
                    }
                    return position;
                });

            // Bar Label
            bar.append("text")
                .attr("class", "barLabel")
                .attr("x", miniX.rangeBand() / 2)
                .attr("y", scope.y(0) + 10)
                .text(_.str.humanize);

            // Bar group label
            chart.append("text")
                .attr("class", "title")
                .attr("x", scope.x.rangeBand() / 2)
                .attr("y", 10 - scope.margin.top)
                .attr("dy", ".75em")
                .text(barsGroupName === 'demand' ? 'Max' : _.str.humanize(barsGroupName));

            var title2 = 'usage';
            if (barsGroupName === 'solar') {
                title2 = 'production';
            } else if (barsGroupName === 'total') {
                title2 = 'bill';
            } else if (barsGroupName === 'demand') {
                title2 = 'demand';
            }

            // Bar group label
            chart.append("text")
                .attr("class", "title")
                .attr("x", scope.x.rangeBand() / 2)
                .attr("y", 30 - scope.margin.top)
                .attr("dy", ".75em")
                .text(title2);

            var units = 'kWh / day';
            if (barsGroupName === 'demand') {
                units = 'kW Demand';
            } else if (barsGroupName === 'total') {
                units = '$ / day';
            }

            // Bar group label
            chart.append("text")
                .attr("class", "units")
                .attr("x", scope.x.rangeBand() / 2)
                .attr("y", 60 - scope.margin.top)
                .attr("dy", ".75em")
                .text(units);

            var yearAnalysis = small.append("g")
                .attr("class", "yearAnalysis");

            var monthAnalysis = small.append("g")
                .attr("class", "monthAnalysis");

            var line1y = 40;
            var r = 2;
            var analysisMargin = 40;
            yearAnalysis.append("line")
                .attr("x1", analysisMargin)
                .attr("x2", scope.x.rangeBand() - analysisMargin)
                .attr("y1", line1y)
                .attr("y2", line1y);

            yearAnalysis.append("circle")
                .attr("cx", analysisMargin)
                .attr("cy", line1y)
                .attr("r", r);

            yearAnalysis.append("circle")
                .attr("cx", scope.x.rangeBand() - analysisMargin)
                .attr("cy", line1y)
                .attr("r", r);

            var yearXshift = scope.x.rangeBand()/2;


            var percentVal;
            if (chartData.last_year) {
                percentVal = 100 * (chartData.this_month - chartData.last_year) / chartData.last_year;
            }

            var percentText = 'N / A';
            if (!_.isUndefined(percentVal)) {
                percentText = Math.round(Math.abs(percentVal)) + '%';
            }

            yearAnalysis.append("text")
                .attr("class", "percent " + classOfChange(barsGroupName, percentVal))
                .text(percentText)
                .attr("transform", "translate(" + yearXshift +  ", " + 15 + ")");

            var changeVal;
            if (chartData.last_year) {
                changeVal = chartData.this_month_money - chartData.last_year_money;
            }

            var changeText = 'N / A';
            if (!_.isUndefined(changeVal)) {
                changeText = '$ ' + Math.round(Math.abs(changeVal)) + " / day";
            }

            yearAnalysis.append("text")
                .attr("class", "value " + classOfChange(barsGroupName, changeVal))
                .text(changeText)
                .attr("transform", "translate(" + yearXshift +  ", " + 30 + ")");

            if (changeVal) {
                var yearArrow = arrowOf(yearAnalysis, barsGroupName, changeVal);
                yearArrow.attr("transform", "translate(" + 0 +  ", " + 5 + "), scale(0.35)");
            }

            var line2y = line1y * 2;
            monthAnalysis.append("line")
                .attr("x1", miniX.rangeBand() + analysisMargin)
                .attr("x2", scope.x.rangeBand() - analysisMargin)
                .attr("y1", line2y)
                .attr("y2", line2y);

            monthAnalysis.append("circle")
                .attr("cx", miniX.rangeBand() + analysisMargin)
                .attr("cy", line2y)
                .attr("r", r);

            monthAnalysis.append("circle")
                .attr("cx", scope.x.rangeBand() - analysisMargin)
                .attr("cy", line2y)
                .attr("r", r);

            var monthXshift = miniX.rangeBand() + ((scope.x.rangeBand() - miniX.rangeBand())/2);

            var percentVal;
            if (chartData.last_month) {
                percentVal = 100 * (chartData.this_month - chartData.last_month) / chartData.last_month;
            }

            var percentText = 'N / A';
            if (!_.isUndefined(percentVal)) {
                percentText = Math.round(Math.abs(percentVal)) + '%';
            }

            monthAnalysis.append("text")
                .attr("class", "percent " + classOfChange(barsGroupName, percentVal))
                .text(percentText)
                .attr("transform", "translate(" + monthXshift +  ", " + (line1y + 15) + ")");

            var changeVal;
            if (chartData.last_month) {
                changeVal = chartData.this_month_money - chartData.last_month_money;
            }

            var changeText = 'N / A';
            if (!_.isUndefined(changeVal)) {
                changeText = '$ ' + Math.round(Math.abs(changeVal)) + " / day";
            }

            monthAnalysis.append("text")
                .attr("class", "value " + classOfChange(barsGroupName, changeVal))
                .text(changeText)
                .attr("transform", "translate(" + monthXshift +  ", " + (line1y + 30) + ")");

            if (changeVal) {
                var monthArrow = arrowOf(monthAnalysis, barsGroupName, changeVal);
                monthArrow.attr("transform", "translate(" + miniX.rangeBand() +  ", " + (line1y + 5) + "), scale(0.35)");
            }

        });

    }

    function controller(scope, element) {
        scope.$watch('dataupdated', function() {
            if (scope.data) {
                plot(scope, element, scope.data);
            }
        });
    }

    angular.module('insightApp')
    .directive('performancegraph', function () {
        return {
            templateUrl: 'views/directives/performancegraph.html',
            replace: true,
            restrict: 'E',
            scope: {
                data: '=',
                dataupdated: '@'
            },
            controller: ['$scope', '$element', controller]
        };
    });

}).call(null);
