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
         $("#tabs").append(
            $('<li>')
            .append(
                $('<a>')
                .attr('data-toggle', 'tab')
                .text('nbnavigator')
            )
        );
    }
    exports.load_ipython_extension = load_ipython_extension;
    return {
        load_ipython_extension: load_ipython_extension
    };
});