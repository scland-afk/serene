module.exports = {
    name: "Serene Construction Landscaping",
    email: "info@serenelandscapes.ca",
    phoneForTel: "587-566-9879",
    phoneFormatted: "587-566-9879",
    address: {
        lineOne: "Edmonton",
        lineTwo: "",
        city: "Edmonton",
        state: "AB",
        zip: "",
        country: "CA",
        mapLink: "https://www.google.com/maps/place/Serene+Construction+Landscaping/data=!4m2!3m1!1s0x0:0x5f20d9850f2b6776",
    },
    socials: {
        facebook: "https://www.facebook.com/profile.php?id=61562052516322",
        instagram: "https://www.instagram.com/serenelandscapingyeg/",
        google: "https://g.page/r/CXZnKw-F2SBfEBM/review",
    },
    //! Make sure you include the file protocol (e.g. https://) and that NO TRAILING SLASH is included
    domain: "https://serenelandscapes.ca",
    // Passing the isProduction variable for use in HTML templates
    isProduction: process.env.ELEVENTY_ENV === "PROD",
};
