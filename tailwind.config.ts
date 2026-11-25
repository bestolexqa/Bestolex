import type { Config } from 'tailwindcss'

export default {
  darkMode: 'class',
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      colors: {
        // ألوان الهوية المعتمدة (دليل الهوية، الإصدار 1.0)
        primary: '#E99E05',   // Construction Gold
        secondary: '#191919', // Charcoal Black
        ink: '#191919',
        slate: '#6F7070',     // Slate Gray
        line: '#E1E3E3',      // حدود البطاقات والجداول
        surface: '#F4F5F5',   // أرضية فصل الأقسام
      },
      fontFamily: {
        sans: ['Tajawal', 'sans-serif'],
        display: ['Changa', 'Tajawal', 'sans-serif'],
      }
    },
  },
  plugins: [],
} satisfies Config
