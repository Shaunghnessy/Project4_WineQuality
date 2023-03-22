$(document).ready(function() {
    console.log("Page Loaded");

    $("#wine_predictions").click(function() {
        // alert("button clicked!");
        wine_predictions();
    });

    function wine_predictions() {
        var fixed_acidity = $("#fixed_acidity").val();
        var volatile_acidity = $("#volatile_acidity").val();
        var citric_acid = $("#citric_acid").val();
        var residual_sugar = $("#residual_sugar").val();
        var chlorides = $("#chlorides").val();
        var free_sulfur_dioxide = $("#free_sulfur_dioxide").val();
        var total_sulfur_dioxide = $("#total_sulfur_dioxide").val();
        var density = $("#density").val();
        var pH = $("#pH").val();
        var sulphates = $("#sulphates").val();
        var alcohol = $("#alcohol").val();

        // check if inputs are valid
        // ...

        // create the payload
        var payload = {
            "fixed acidity": fixed_acidity,
            "volatile acidity": volatile_acidity,
            "citric acid": citric_acid,
            "residual sugar": residual_sugar,
            "chlorides": chlorides,
            "free sulfur dioxide": free_sulfur_dioxide,
            "total sulfur dioxide": total_sulfur_dioxide,
            "density": density,
            "pH": pH,
            "sulphates": sulphates,
            "alcohol": alcohol
        };

        // Perform a POST request to the query URL
        $.ajax({
            type: "POST",
            url: "/wine_predictions",
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({ "data": payload }),
            success: function(returnedData) {
                // print it
                console.log(returnedData);

                if (returnedData["prediction"] === "Good") {
                    $("#output").text("That is some good Wine Homie!");
                } else {
                    $("#output").text("Save it for those annoying people you don't like. :(");
                }

            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Status: " + textStatus);
                alert("Error: " + errorThrown);
            }
        });
    }
});