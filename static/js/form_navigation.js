document.addEventListener("DOMContentLoaded", function () {
    const steps = document.querySelectorAll(".form-step")
    const nextButtons = document.querySelectorAll(".next-step");
    const prevButtons = document.querySelectorAll(".prev-step");
    let currentStep = 0;
    

    function showStep(step) {
        steps.forEach((s, index) => {
            s.classList.toggle("active", index === step);
        });
    }


    nextButtons.forEach(button => {
        button.addEventListener("click", function () {
            if (currentStep < steps.length - 1) {
                currentStep++;
                showStep(currentStep);
            }
        });
    });

    prevButtons.forEach(button => {
        button.addEventListener("click", function () {
            if (currentStep > 0) {
                currentStep--;
                showStep(currentStep);
            }
        });
    });

    

    showStep(currentStep)
})


function toggleExtraDeliverables() {

    const extra = document.getElementById("extra-deliverables");
    if (extra.style.display === "none") {
        extra.style.display = "block";
    } else {
        extra.style.display = "none";
    }
}

function toggleTaskDeliverables(){

     const extra = document.getElementById("extra-task");
    if (extra.style.display === "none") {
        extra.style.display = "block";
    } else {
        extra.style.display = "none";
    }

}


function toggleRiskkDeliverables(){

    const extra = document.getElementById("extra-risk");
    if (extra.style.display === "none") {
        extra.style.display = "block";
    } else {
        extra.style.display = "none";
    }

}


function toggleStackDeliverables(){

    const extra = document.getElementById("extra-stack");
    if (extra.style.display === "none") {
        extra.style.display = "block";
    } else {
        extra.style.display = "none";
    }

}