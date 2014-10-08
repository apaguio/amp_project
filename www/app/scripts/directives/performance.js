/* jshint quotmark: false */
/* global d3, _ */
'use strict';

(function() {

    var duration = 4900;
    var bisectDate = d3.bisector(function(d) { return d.time; }).left;

    function plot(scope, el, data) {

        if (!data) {
            return;
        }

        var total = {
            last_year: 0,
            last_month: 0,
            this_month: 0
        };

        _.each(data, function(v, k) {
            if (k !== 'solar') {
                total.last_year += v.last_year;
                total.last_month += v.last_month;
                total.this_month += v.this_month;
            } else {
                total.last_year -= v.last_year;
                total.last_month -= v.last_month;
                total.this_month -= v.this_month;
            }
        });

        data.total = total;

        scope.yBegining = el[0].getBoundingClientRect().top;
        scope.margin = {top: 100, right: 0, bottom: 20, left: 40, between: 30};
        scope.width = el.width() - scope.margin.right - scope.margin.left;
        scope.height = el.height() - scope.margin.top - scope.margin.bottom;
        scope.bigheight = scope.height * 2 / 3;
        scope.smallheight = (scope.height / 3) - scope.margin.between;

        var maxValue = _(data).values().map(function(d) {
            return _.values(d);
        }).flatten().max().value();
        
        scope.x = d3.scale.ordinal().rangeRoundBands([0, scope.width - scope.margin.left - scope.margin.right], .1);
        scope.x.domain(_.keys(data));

        scope.y = d3.scale.linear().range([scope.bigheight, 0]);
        scope.y.domain([0, maxValue + 20]);

        scope.svg = d3.select(el[0]).select(".graph").append("svg")
            .attr("width", scope.width + scope.margin.left + scope.margin.right)
            .attr("height", scope.height + scope.margin.top + scope.margin.bottom);

        var gradient = scope.svg.append("svg:defs")
            .append("svg:linearGradient")
            .attr("id", "gradient")
            .attr("x1", "0")
            .attr("y1", "0")
            .attr("x2", "0")
            .attr("y2", "1")
            .attr("spreadMethod", "pad");

        gradient.append("svg:stop")
            .attr("offset", "0%")
            .attr("stop-color", d3.rgb(179, 204, 253)) // Light blue
            .attr("stop-opacity", 1);

        gradient.append("svg:stop")
            .attr("offset", "100%")
            .attr("stop-color", d3.rgb(106, 149, 212)) // dark blue
            .attr("stop-opacity", 1);

        var mainChart = scope.svg.append("g")
            .attr("class", "mainChart")
            .attr("transform", "translate(" + scope.margin.left + "," + scope.margin.top + ")");

        var miniChart = mainChart.selectAll("g") 
            .data(_.keys(data))
            .enter()
            .append("g")
            .attr("class", function(d) { return d; })
            .attr("transform", function(d) { return "translate(" + scope.x(d) + ",0)"; });

        var miniX = d3.scale.ordinal().rangeRoundBands([0, scope.x.rangeBand()], .1);

        miniChart.each(function(barsGroupName) {

            var chartData = data[barsGroupName];
            miniX.domain(_.keys(chartData));

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

            var bar = chart.selectAll("g")
                .data(_.keys(chartData)).enter()
                .append("g")
                .attr("class", function(d) { return d; })
                .attr("transform", function(d) { return "translate(" + miniX(d) + ",0)"; });

            bar.append("rect")
                .attr("y", function(d) { return scope.y(chartData[d]); })
                .attr("height", function(d) { return scope.bigheight - scope.y(chartData[d]); })
                .attr("width", miniX.rangeBand())
                .style("fill", "url(#gradient)");

            // Bar value
            bar.append("text")
                .attr("x", miniX.rangeBand() / 2)
                .attr("y", function(d) { return scope.y(chartData[d]) - 15; })
                .attr("dy", ".75em")
                .text(function(d) { return (chartData[d] || 0).toFixed(3); });

            // Bar Label
            bar.append("text")
                .attr("x", miniX.rangeBand() / 2)
                .attr("y", function(d) { return scope.y(0) + 10; })
                .attr("dy", ".75em")
                .text(_.str.humanize);

            // Bar group label
            chart.append("text")
                .attr("class", "title")
                .attr("x", scope.x.rangeBand() / 2)
                .attr("y", 10 - scope.margin.top)
                .attr("dy", ".75em")
                .text(_.str.humanize(barsGroupName));

            var title2 = 'usage';
            if (barsGroupName === 'solar') {
                title2 = 'production';
            } else if (barsGroupName === 'total') {
                title2 = 'bill';
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
                units = '';
            }

            // Bar group label
            chart.append("text")
                .attr("class", "units")
                .attr("x", scope.x.rangeBand() / 2)
                .attr("y", 60 - scope.margin.top)
                .attr("dy", ".75em")
                .text(units);

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
