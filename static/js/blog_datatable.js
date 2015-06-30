;(function ($) {

    // Set the defaults
    var pluginName = 'BlogDataTable',
        defaults = {
            dataTable_plugin: null,
            msg_search: ""
        };

    var BlogDataTable = function (element, options){
        this.init(element, options);
    };

    BlogDataTable.prototype = {

        constructor: BlogDataTable,

        init: function (element, options){
            this.$element = $(element);
            this.options = $.extend( {}, defaults, options) ;

            this.add_bootstrap();
        },

        add_bootstrap: function(){
            var $search_input = this.$element.find(".dataTables_filter input");
            // Remove the content of the label, and the label itself
            this.$element.find(".dataTables_filter label").contents().filter(function(){ return this.nodeType != 1; }).remove();
            $search_input.unwrap();
            $search_input.addClass("form-control");
            $search_input.prop("id","search-draw" );
            $search_input.prop("placeholder",this.options.msg_search );
            $search_input.parent().addClass("col-xs-12");
            $search_input.wrap( "<div class='input-group'></div>" );
            $search_input.after("<span class='input-group-btn'><button class='btn btn-default' type='button'><span class='glyphicon glyphicon-search'></span></button></span>");
        }
    };

    $.fn.blogDataTable = function (option, param) {
        this.each(function () {
            var $this = $(this)
                , data = $this.data('plugin_' + pluginName)
                , options = typeof option == 'object' && option

            if (typeof option === 'string') {
                data[option].apply(data, ['no_animation'])
            } else {
                if (!data && typeof option !== 'string' && !param) {
                    $this.data('plugin_' + pluginName, (new BlogDataTable(this, options)))
                }
            }
        })
    }

    $.fn.outerHTML = function() {
      return jQuery('<div />').append(this.eq(0).clone()).html();
    };

})(window.jQuery, window, document );

$(document).ready(function () {
// Fill the datatable
    var $panel_articles = $('#panel-articles').dataTable(
    {
        "bJQueryUI": true,
        "language" : {
            "emptyTable":     "No data available in table",
            "info":           "Showing _START_ to _END_ of _TOTAL_ entries",
            "infoEmpty":      "Showing 0 to 0 of 0 entries",
            "infoFiltered":   "(filtered from _MAX_ total entries)",
            "thousands":      ",",
            "lengthMenu":     "Show _MENU_ entries",
            "loadingRecords": "Loading...",
            "processing":     "Processing...",
            "search":         "Search:",
            "zeroRecords":    "No matching records found",
            "paginate": {
                "first":      "First",
                "last":       "Last",
                "next":       "Next",
                "previous":   "Previous"
            },
            "aria": {
                "sortAscending":  ": activate to sort column ascending",
                "sortDescending": ": activate to sort column descending"
            }
        },
        "order": [[ 1, "desc" ]],
        "lengthMenu": [[5, 10, 25, -1], [5, 10, 25, "All"]],
        "columnDefs": [
        { "width": "100px", "targets": 0, "sortable": true },
        { "targets": 1, "serchable": true },
        { "targets": 2, "serchable": true },
        { "width": "30px", "targets": 3, "serchable": true },
        ]
    }
    );

    // Add blog_datatable plugin to the table
    $('#panel-articles_wrapper').blogDataTable({
        "dataTable_plugin": $panel_articles,
        "msg_search": "Search..."
    });

});





