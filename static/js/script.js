document.addEventListener("DOMContentLoaded", () => {
  if (window.location.pathname.indexOf("/challenge/") > -1) {
    const foundItForm = document.querySelector(".found-it-form");
    const foundItButton = document?.querySelector(".found-it");
    const skipButton = document?.querySelector(".skip");
    const scoreInput = document.querySelector("input[name='score']");

    foundItButton.addEventListener("click", async (event) => {
      event.preventDefault();

      try {
        toggleLoadingSpinner();
        const challengeCoordinates = await getChallengeCoordinates();
        const userCoordinates = await getLocation();

        const distance = getDistanceFromLatLonInKm(
          challengeCoordinates.latitude,
          challengeCoordinates.longitude,
          userCoordinates.latitude,
          userCoordinates.longitude
        );

        if (distance < 0.05) {
          scoreInput.value = 1;
          displaySuccessOrFailModal('CONGRATS! \n🥳', 'You earned one point for finding this location!', 'Dismiss');
          foundItForm.submit();
        } else {
          // display not close enough message
          displaySuccessOrFailModal('Not close enough yet! \n😬', 'You need to be within 50 meters of the challenge to find it.', 'Try again');
        }

        console.log(distance.toFixed(2));
      } catch (error) {
        console.error(error);
        // Handle error appropriately
      }
      toggleLoadingSpinner();
    });

    skipButton.addEventListener("click", (event) => {
      event.preventDefault();
      scoreInput.value = -1;
      foundItForm.submit();
    });
  }
});

/*
 * Function that requests access to
 * the user's location and returns
 * the coordinates
 */
const getLocation = () =>
  new Promise((resolve, reject) => {
    const showPosition = (position) => {
      const { latitude, longitude } = position.coords;
      resolve({ latitude, longitude });
    };

    const showError = (error) => reject(error);

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
      reject(new Error("Geolocation is not supported by this browser."));
    }
  });

/*
 * Function that fetches the coordinates
 * of the challenge
 */
const getChallengeCoordinates = async () => {
  let urlNum = window.location.pathname.split("/")[2];
  
  const response = await fetch(`${window.location.origin}/json/${urlNum}/`, {
    headers: {
      Accept: "application/json",
      "X-Requested-With": "XMLHttpRequest",
    },
  });

  const data = await response.json();
  let [latitude, longitude] = data.coordinates.split(",");

  // convert latitude and longitude to floats
  latitude = parseFloat(latitude);
  longitude = parseFloat(longitude);

  return { latitude, longitude };
};

/*
 * Function that calculates the distance
 * between two coordinates
 * Source: https://stackoverflow.com/a/27943/12327909
 */
const getDistanceFromLatLonInKm = (lat1, lon1, lat2, lon2) => {
  const radius = 6371; // Radius of the earth in km
  const distanceLat = deg2rad(lat2 - lat1); // deg2rad below
  const distanceLon = deg2rad(lon2 - lon1);
  const a =
    Math.sin(distanceLat / 2) * Math.sin(distanceLat / 2) +
    Math.cos(deg2rad(lat1)) *
      Math.cos(deg2rad(lat2)) *
      Math.sin(distanceLon / 2) *
      Math.sin(distanceLon / 2);

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  const distance = radius * c; // Distance in km

  return distance;
};

/*
 * Function that converts degrees to radians
 * Source: https://stackoverflow.com/a/27943/12327909
 */
const deg2rad = (deg) => deg * (Math.PI / 180);

/*
 * Function that toggles a loading spinner
 * overlay on the page
 */
const toggleLoadingSpinner = () => {
  if (document.querySelector(".overlay")) {
    document.querySelector(".overlay").remove();
  } else {
    // create overlay
    const overlay = document.createElement("div");
    overlay.classList.add("overlay");

    // spinner container
    const spinnerContainer = document.createElement("div");
    spinnerContainer.classList.add("spinner-container");

    // create spinner
    const spinner = document.createElement("div");
    spinner.classList.add("spinner");

    // spinner text
    let spinnerText = document.createElement("p");
    spinnerText.classList.add("spinner-text");
    spinnerText.innerText = "Checking your location";

    const loadingDots = () => {
      if (spinnerText.innerText == "Checking your location...") {
        spinnerText.innerText = "Checking your location";
      } else {
        spinnerText.innerText += ".";
      }
    };

    setInterval(loadingDots, 500);

    // append spinner to spinner container
    spinnerContainer.appendChild(spinner);

    // append spinner text to spinner container
    spinnerContainer.appendChild(spinnerText);

    // append spinner to overlay
    overlay.appendChild(spinnerContainer);

    // append overlay to body
    document.body.appendChild(overlay);
  }
};

const displaySuccessOrFailModal = (headingText, paragraphText, buttonText) => {
  const dialog = document.createElement('dialog');
  
  const heading = document.createElement('h2');
  heading.classList.add('text-center', 'display-3');
  heading.innerText = headingText;

  const message = document.createElement('p');
  message.innerText = paragraphText;
  message.classList.add('mb-4', 'text-center');

  const submitButton = document.createElement('button');
  submitButton.innerText = buttonText;
  submitButton.classList.add('btn', 'btn-success', 'w-100');

  // Dismiss the dialog when the "Submit" button is clicked
  submitButton.addEventListener('click', () => {
    dialog.close();
  });

  dialog.appendChild(heading);
  dialog.appendChild(message);
  dialog.appendChild(submitButton);

  document.body.appendChild(dialog);
  dialog.showModal();
};


