document.addEventListener("DOMContentLoaded", function () {
  function setProgress(elementId, percentage, projectName, userName, itemId) {
    const greenCircle = document.querySelector(`#${elementId} .progress-ring`); // Green (progress)
    const text = document.querySelector(`#${elementId} .progress-text`);
    const project_name = document.querySelector(`#${elementId} .project-name`);
    const circumference = 314; // 2 * π * r (where r=50)

    if (!greenCircle || !text) {
      console.error(`Element with ID ${elementId} not found`);
      return;
    }

    const greenProgress = (percentage / 100) * circumference; // Green part for progress
    greenCircle.style.strokeDashoffset = circumference - greenProgress; // Show green progress

    text.textContent = `${percentage}%`;
    project_name.textContent = `${projectName} - ${userName}`;
    project_name.href = `/admin-modify-employee-project/${itemId}`;
  }

  console.log(departmentId);
  

  // Fetch progress values from Django
  fetch(`/get-progress/${departmentId}/`)
    .then((response) => response.json())
    .then((data) => {
      data.forEach((item, index) => {
        setProgress(
          `circle-${index}`,
          item.progress,
          item.project_name,
          item.project_user_name,
          item.id
        );
      });
    })
    .catch((error) => console.error("Error fetching progress:", error));
});
