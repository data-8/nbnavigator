define([
    'base/js/namespace',
    'jquery',
    'exports'
], function(
    Jupyter,
    $,
    exports
) {
    function load_ipython_extension() {
        console.log(
            'This is the current notebook application instance:',
            Jupyter.notebook
        );
        var tab_id = 'nbnavigator'
        $('<div/>')
            .attr('id', tab_id)
            .addClass('tab-pane')
            .text('hello world')
            .appendTo('.tab-content');

         $("#tabs").append(
            $('<li>')
            .append(
                $('<a>')
                .attr('href', '#' + tab_id)
                .attr('data-toggle', 'tab')
                .text('nbnavigator')
                .on('click', function (evt) {
                    window.history.pushState(null, null, '#' + tab_id);
                })
            )
        );
    }
    exports.load_ipython_extension = load_ipython_extension;
    return {
        load_ipython_extension: load_ipython_extension
    };
});