define([
    'base/js/namespace',
    'jquery'
], function(
    Jupyter,
    $
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
                .attr('href', '#assignments')
                .attr('data-toggle', 'tab')
                .text('Assignments')
                .click(function (e) {
                    window.history.pushState(null, null, '#assignments');
                })
            )
        );
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});