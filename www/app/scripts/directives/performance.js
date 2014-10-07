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

        scope.yBegining = el[0].getBoundingClientRect().top;
        scope.margin = {top: 6, right: 0, bottom: 20, left: 40, between: 30};
        scope.width = el.width() - scope.margin.right - scope.margin.left;
        scope.height = el.height() - scope.margin.top - scope.margin.bottom;
        scope.bigheight = scope.height * 2 / 3;
        scope.smallheight = (scope.height / 3) - scope.margin.between;

        scope.x = d3.scale.ordinal().rangeRoundBands([0, scope.width - scope.margin.left - scope.margin.right], .1);
        scope.x.domain(_.keys(data));

        var maxValue = _(data).values().map(function(d) {
            return _.values(d);
        }).flatten().max().value();
        
        scope.y = d3.scale.linear().range([scope.bigheight, 0]);
        scope.y.domain([0, maxValue + 20]);

        scope.svg = d3.select(el[0]).select(".graph").append("svg")
            .attr("width", scope.width + scope.margin.left + scope.margin.right)
            .attr("height", scope.height + scope.margin.top + scope.margin.bottom);

        var miniChart = scope.svg.selectAll("g") 
            .data(_.keys(data))
            .enter()
            .append("g")
            .attr("class", function(d) { return d; })
            .attr("transform", function(d) { return "translate(" + scope.x(d) + ",0)"; });

        var miniX = d3.scale.ordinal().rangeRoundBands([0, scope.x.rangeBand()], .1);

        miniChart.each(function(d) {

            var chartData = data[d];
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
                .attr("width", miniX.rangeBand());

            bar.append("text")
                .attr("x", miniX.rangeBand() / 2)
                .attr("y", function(d) { return scope.y(chartData[d]) + 3; })
                .attr("dy", ".75em")
                .text(function(d) { return chartData[d]; });

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
