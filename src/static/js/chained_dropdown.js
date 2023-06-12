// function getSemesterYear(level_id) {
//     let $ = django.jQuery;
//     $.get('/graduate/sem-year/' + level_id, function (resp) {
//         let sem_year_list = '<option value="" selected="">----Select Semester-----</option>'
//         $.each(resp.data, function (i, item) {
//             sem_year_list += '<option value="' + item.id + '">' + item.sem_year_num + '</option>'
//         });
//         $('#id_sem_year').html(sem_year_list);
//     });
// }

function getSemesterYear(level_id) {
    let $ = django.jQuery;
    console.log("function called")
    $.get('/graduate/sem-year/' + level_id, function (resp) {
        let sem_year_list = '<option value="" selected>----Select Semester-----</option>';
        $.each(resp.data, function (i, item) {
            sem_year_list += '<option value="' + item.id + '">' + item.sem_year_num + '</option>';
        });
        $('#id_sem_year').html(sem_year_list);
        $('#id_sem_year').prop('disabled', false);
    });
}



function getMaterialType(level_id) {
    let $ = django.jQuery;
    $.get('/graduate/material-type/' + level_id, function (resp) {
        let material_type_list = '<option value="" selected="">----Select Material-----</option>'
        $.each(resp.data, function (i, item) {
            material_type_list += '<option value="' + item.id + '">' + item.material_name + '</option>'
        });
        $('#id_material_type').html(material_type_list);
    });
}


function getSubject(level_id) {
    let $ = django.jQuery;
    $.get('/graduate/subject/' + level_id, function (resp) {
        let subject_list = '<option value="" selected="">----Select Subject-----</option>'
        $.each(resp.data, function (i, item) {
            subject_list += '<option value="' + item.id + '">' + item.subject_name + '</option>'
        });
        $('#id_subject').html(subject_list);
    });
}