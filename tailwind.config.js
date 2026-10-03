/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        begonia: {
          50: '#f2f8ee',
          100: '#dfeed3',
          400: '#6fae4e',
          600: '#438F17',
          700: '#3b6529',
          800: '#2e4f20',
          900: '#be185d',
        },
      },
      fontFamily: {
        display: ['Poppins', 'Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}