// some jquery methods to interact with index.html
$(document).ready(function() {
    // example queries
    var select_all_query = "SELECT * FROM student;";
    var insert_query = "INSERT INTO student (name, nr) VALUES (\"Peter Pan\", 4444);";
    var update_query = "UPDATE student SET name=\"Arnold Schwarzenegger\", nr=800 WHERE id=2;";
    var delete_query = "DELETE FROM student WHERE id=1;";

    var modal = document.getElementById("myModal");
    var modal_content = document.getElementById("modal_content");

    var span = document.getElementsByClassName("close")[0];

    $("#select_all_query").click(function(event) {
        $('#queryArea').val(select_all_query);
    });

    $("#insert_query").click(function(event) {
        $('#queryArea').val(insert_query);
    });

    $("#update_query").click(function(event) {
        $('#queryArea').val(update_query);
    });

    $("#delete_query").click(function(event) {
        $('#queryArea').val(delete_query);
    });

    // call the REST API and show results
    $("#run_query").click(function(event) {
        call = "./run?query=" + escape($('#queryArea').val())
        $.get(call, function(data, status){
            var jsonObj = JSON.parse(data);
            var jsonPretty = JSON.stringify(jsonObj, null, '\t');

            modal.style.display = "block";
            $("#modal_content").text(jsonPretty);
        });
    });

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});



