/* jshint quotmark: false */
/* global d3, _ */
'use strict';

(function() {

    var duration = 1000;

    function signOfChange(group, value) {
        if (group === "solar") {
            if (_.isUndefined(value)) {
                return "";
            }
            return value < 0 ? " - " : " + ";
        }
        if (_.isUndefined(value)) {
            return "";
        }
        return value > 0 ? " - " : " + ";
    }

    function classOfChange(group, value) {
        if (group === "solar") {
            if (_.isUndefined(value)) {
                return "green";
            }
            return value < 0 ? "red" : "green";
        }
        if (_.isUndefined(value)) {
            return "red";
        }
        return value > 0 ? "red" : "green";
    }

    function updateData(originalData) {
        _.each(originalData, function(v) {
            v.this_month_money = v.charges.this_month;
            v.last_month_money = v.charges.last_month;
            v.last_year_money = v.charges.last_year || (v.charges.this_month_money + ( v.charges.this_month_money * 20));
            delete v.charges;
        });
        return originalData;
    }

    function fakeData(originalData) {
        _.each(originalData, function(data, k) {
            data.last_year = data.last_month + ( data.last_month / 20);
            data.last_year_money = data.last_month_money + ( data.last_month_money/ 20);
            //data.last_month = data.this_month + ( data.this_month / 10);
            if (k === 'solar') {
                data.last_year = 0;
                data.last_year_money = 0;
                //data.last_month = data.this_month - ( data.this_month / 10);
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
        scope.width = (el.width() || el.parent().width()) - scope.margin.right - scope.margin.left;
        scope.height = el.height() - scope.margin.top - scope.margin.bottom;
        scope.bigheight = scope.height * 2 / 3;
        scope.smallheight = (scope.height / 3) - scope.margin.between;

        var maxValue = _(data).values().map(function(d) {
            return [d.last_year, d.last_month, d.this_month];
        }).flatten().max().value();

        var maxDemandValue = _(data.demand).values().max().value();
        //maxValue += _.max([data.solar.last_month, data.solar.last_year, data.solar.this_month]);

        data.total = total;
        var maxTotalValue = _.max([
                data.total.last_month_money + data.solar.last_month_money,
                data.total.last_year_money + data.solar.last_year_money,
                data.total.this_month_money + data.solar.this_month_money]);
        
        var miniChartDomain = ['energy', 'demand', 'solar', 'total'];
        //var miniChartDomain = _.keys(data);
        scope.x = d3.scale.ordinal().rangeRoundBands([0, scope.width - scope.margin.left - scope.margin.right], 0.1);
        // To preserve the order
        scope.x.domain(miniChartDomain);

        scope.y = d3.scale.linear().range([scope.bigheight, 0]);
        scope.y.domain([0, maxValue]);

        scope.yTotal = d3.scale.linear().range([scope.bigheight, 0]);
        scope.yTotal.domain([0, maxTotalValue]);

        scope.yMaxDemand = d3.scale.linear().range([scope.bigheight, 0]);
        scope.yMaxDemand.domain([0, maxDemandValue]);

        scope.svg = d3.select(el[0]).select(".performancegraph").append("svg")
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

        var miniX = d3.scale.ordinal().rangeRoundBands([0, scope.x.rangeBand()], 0.3);

        miniChart.each(function(barsGroupName) {

            var yScale = scope.y;
            if (barsGroupName === 'demand') {
                yScale = scope.yMaxDemand;
            } else if (barsGroupName === 'total') {
                yScale = scope.yTotal;
            }
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
                    .attr("x2", function() { return scope.x.rangeBand(); })
                    .attr("y1", scope.bigheight)
                    .attr("y2", scope.bigheight);
            }


            var small = chart.append("g")
                .attr("class", "small")
                .attr("transform", "translate(0, " + ( scope.bigheight + scope.margin.between) + ")");

            var bar = chart.selectAll("g.barGroup")
                .data(barsDomain).enter()
                .append("g")
                .attr("class", function(d) { return "barGroup " + d; })
                .attr("transform", function(d) { return "translate(" + miniX(d) + ",0)"; });

            if (barsGroupName === 'total') {
                bar.append("rect")
                    .attr("class", "energy")
                    .attr("y", scope.bigheight)
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var energy = yScale(data.energy[m] || 0);
                        return energy;
                    })
                    .attr("height", function(d) {
                        var m = d + '_money';
                        var energy = yScale(data.energy[m] || 0);
                        return scope.bigheight - energy;
                    });

                bar.append("text")
                    .attr("class", "energy_val")
                    .attr("x", miniX.rangeBand()/2)
                    .attr("y", scope.bigheight)
                    //.attr("height", function(d) { return scope.bigheight - yScale(data.energy[d] || 0); })
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var energy = yScale(data.energy[m] || 0);
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
                        var energy = yScale(data.energy[m] || 0);
                        return energy;
                    })
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .delay(duration)
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var energy = scope.bigheight - yScale(data.energy[m] || 0);
                        var demand = yScale(data.demand[m] || 0);
                        var position = demand - energy;
                        return position;
                    })
                    .attr("height", function(d) {
                        var m = d + '_money';
                        var demand = yScale(data.demand[m] || 0);
                        return scope.bigheight - demand;
                    });

                bar.append("text")
                    .attr("class", "demand_val")
                    .attr("x", miniX.rangeBand()/2)
                    .attr("y",  function(d) {
                        var m = d + '_money';
                        var energy = yScale(data.energy[m] || 0);
                        return energy + 15;
                    })
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .delay(duration)
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var energy = scope.bigheight - yScale(data.energy[m] || 0);
                        var demand = yScale(data.demand[m] || 0);
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
                        var demand = scope.bigheight - yScale(data.demand[m] || 0);
                        var energy = yScale(data.energy[m] || 0);
                        var position = energy - demand;
                        return position;
                    })
                    //.attr("height", function(d) { return scope.bigheight - yScale(data.solar[d] || 0); })
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .delay(2 * duration)
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var solar = scope.bigheight - yScale(data.solar[m] || 0);
                        var demand = scope.bigheight - yScale(data.demand[m] || 0);
                        var energy = scope.bigheight - yScale(data.energy[m] || 0);
                        var position = scope.bigheight - solar - energy - demand;
                        return position;
                    })
                    .attr("height", function(d) { return scope.bigheight - yScale(data.solar[d + '_money'] || 0); });

                bar.append("text")
                    .attr("class", "solar_val")
                    .attr("x", miniX.rangeBand()/2)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var demand = scope.bigheight - yScale(data.demand[m] || 0);
                        var energy = yScale(data.energy[m] || 0);
                        var position = energy - demand;
                        return position;
                    })
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .delay(2 * duration)
                    .duration(duration)
                    .attr("y", function(d) {
                        var m = d + '_money';
                        var solar = scope.bigheight - yScale(data.solar[m] || 0);
                        var demand = scope.bigheight - yScale(data.demand[m] || 0);
                        var energy = scope.bigheight - yScale(data.energy[m] || 0);
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
                        var height = scope.bigheight - yScale(chartData[d] || 0);
                        var position = yScale(chartData[d] || 0);
                        return height + position;
                    })
                    .attr("height", 0)
                    .attr("width", miniX.rangeBand())
                    .transition()
                    .duration(duration)
                    .attr("y", function(d) {
                        var position = yScale(chartData[d] || 0);
                        return position;
                    })
                    .attr("height", function(d) {
                        return scope.bigheight - yScale(chartData[d] || 0);
                    });
            }

            // Bar value
            bar.append("text")
                .attr("x", miniX.rangeBand() / 2)
                .attr("y", function() { return scope.bigheight - 15; })
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
                    var position =  yScale(chartData[d]) - 15;
                    if (barsGroupName === 'total') {
                        var m = d + '_money';
                        position = yScale(chartData[m] + data.solar[m]) - 15;
                    }
                    return position;
                });

            // Bar Label
            bar.append("text")
                .attr("class", "barLabel")
                .attr("x", miniX.rangeBand() / 2)
                .attr("y", yScale(0) + 10)
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
            var yearXshift = scope.x.rangeBand()/2;

            var changeValCharges = 0;
            var percentText = 'N / A';
            var changeText = 'N / A';
            if (!_.isUndefined(chartData.last_year_money)) {
                if (chartData.last_year_money !== 0) {
                    changeValCharges = chartData.this_month_money - chartData.last_year_money;
                    var percentVal = 100 * changeValCharges / chartData.last_year_money;
                    var sign = signOfChange(barsGroupName, changeValCharges);
                    percentText = sign + Math.round(Math.abs(percentVal)) + '%';
                    changeText = sign + ' $ ' + Math.round(Math.abs(changeValCharges)) + " / day";
                }
            }

            yearAnalysis.append("text")
                .attr("class", "percent " + classOfChange(barsGroupName, changeValCharges))
                .text(percentText)
                .attr("transform", "translate(" + yearXshift +  ", " + 15 + ")");

            yearAnalysis.append("text")
                .attr("class", "value " + classOfChange(barsGroupName, changeValCharges))
                .text(changeText)
                .attr("transform", "translate(" + yearXshift +  ", " + 30 + ")");

            var monthXshift = miniX.rangeBand() + ((scope.x.rangeBand() - miniX.rangeBand())/2);

            var monthChangeValCharges = 0;
            var monthPercentText = 'N / A';
            var monthChangeText = 'N / A';
            if (!_.isUndefined(chartData.last_month_money)) {
                if (chartData.last_month_money) {
                    monthChangeValCharges = chartData.this_month_money - chartData.last_month_money;
                    var sign = signOfChange(barsGroupName, monthChangeValCharges);
                    var monthPercentVal = 100 * monthChangeValCharges / chartData.last_month_money;
                    monthPercentText = sign + Math.round(Math.abs(monthPercentVal)) + '%';
                    monthChangeText = sign + ' $ ' + Math.round(Math.abs(monthChangeValCharges)) + " / day";
                }
            }

            monthAnalysis.append("text")
                .attr("class", "percent " + classOfChange(barsGroupName, monthChangeValCharges))
                .text(monthPercentText)
                .attr("transform", "translate(" + monthXshift +  ", " + (line1y + 15) + ")");

            monthAnalysis.append("text")
                .attr("class", "value " + classOfChange(barsGroupName, monthChangeValCharges))
                .text(monthChangeText)
                .attr("transform", "translate(" + monthXshift +  ", " + (line1y + 30) + ")");
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
