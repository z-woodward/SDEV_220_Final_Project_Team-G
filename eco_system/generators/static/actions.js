/**
 * @Author: Donald Osgood
 * @Date:   2023-11-24 13:35:30
 * @Last Modified by:   Donald Osgood
 * @Last Modified time: 2023-11-24 22:45:58
 */

/**
 * Retrieves input data from a form and returns it as a JSON object.
 * @param  {HTMLFormControlsCollection} elements  the form elements
 * @return {Object}                               form data as an object literal
 */
const formToJSON = (elements) =>
  [].reduce.call(
    elements,
    (data, element) => {
      data[element.name] = element.value;
      return data;
    },
    {}
  );


function generateStrings(endpoint, form_id) {
  try {
    const formItem = document.getElementById(form_id);
    const formData = new FormData(formItem);
    fetch(endpoint,{
        "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "body": JSON.stringify(Object.fromEntries(formData))
    })
      .then((response) => response.json())
      .then((data) => {
        const formResults = document.getElementById("results");
        formResults.innerHTML = data.results
        // data is a parsed JSON object
      });
  } catch (error) {
    return false;
  }
  return false;
}
