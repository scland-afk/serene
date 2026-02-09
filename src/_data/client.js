module.exports = {
    name: "Serene Landscaping",
    email: "info@serenelandscapes.ca",
    phoneForTel: "587-566-9879",
    phoneFormatted: "(587) 566-9879",
    address: {
        lineOne: "Edmonton",
        lineTwo: "",
        city: "Edmonton",
        state: "AB",
        zip: "",
        country: "CA",
        mapLink: "https://maps.app.goo.gl/Jr11RghBbpAnZkLX9",
    },
    socials: {
        facebook: "https://www.facebook.com/profile.php?id=61562052516322",
        instagram: "https://www.instagram.com/serenelandscapingyeg/",
        google: "https://share.google/lLS8npO0pjtyaF1D2",
    },
    //! Make sure you include the file protocol (e.g. https://) and that NO TRAILING SLASH is included
    domain: "https://serenelandscapes.ca",
    // Passing the isProduction variable for use in HTML templates
    isProduction: process.env.ELEVENTY_ENV === "PROD",
};
