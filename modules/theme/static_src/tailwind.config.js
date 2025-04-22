/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

const colors = require("tailwindcss/colors");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../../shared/src/common/presentation/**/*.*",
    "../../authentication/src/presentation/**/*.*",
    "../../tasks/src/presentation/**/*.*",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../../**/node_modules',
    "./node_modules/flowbite/**/*.js",
    /* JS 2: Process all JavaScript files in the project. */
    // '../../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    "../../../**/*.py",
  ],
  theme: {
    extend: {},
    screens: {
      xs: "512px",
      "xs-sm": "576px",
      sm: "640px",
      "sm-md": "704px",
      md: "768px",
      "md-lg": "896px",
      lg: "1024px",
      "lg-xl": "1152px",
      xl: "1280px",
      "xl-2xl": "1408px",
      "2xl": "1536px",
    },
    colors: {
      ...colors,
      marrs: {
        100: "#cffffc",
        200: "#a3fff9",
        300: "#7cfef5",
        400: "#27d7ce",
        500: "#1dada5",
        600: "#14847e",
        700: "#0b5d59",
        800: "#043a37",
        900: "#011917",
      },
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    // require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
    require("flowbite/plugin"),
  ],
};
