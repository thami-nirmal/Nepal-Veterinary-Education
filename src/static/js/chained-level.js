function getSemYear(level_id) {
    let $ = django.jQuery;
    $.get('/graduate/sem-year/' + level_id, function (resp){
        let sem_year_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           sem_year_list += '<option value="'+ item.id +'">'+ item.sem_year_name +'</option>'
        });
        $('#id_sem_year').html(sem_year_list);
    });
}