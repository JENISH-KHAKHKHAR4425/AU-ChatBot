// Firebase modules for Auth
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup } 
from "https://www.gstatic.com/firebasejs/9.23.0/firebase-auth.js";

// Firebase config
const firebaseConfig = {
    apiKey: "AIzaSyC6UUXB0OG6zxvGePmXltPjE-c8Hg-t8T8",
    authDomain: "atmiya-university---chatbot.firebaseapp.com",
    projectId: "atmiya-university---chatbot",
    storageBucket: "atmiya-university---chatbot.firebasestorage.app",
    messagingSenderId: "953500059940",
    appId: "1:953500059940:web:4df148b9f980f22d298bb1",
    measurementId: "G-5D8G35CPSL"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Google provider
const googleProvider = new GoogleAuthProvider();

// ================= GOOGLE SIGN-IN =================
window.googleSignIn = async function () {
    try {
        const result = await signInWithPopup(auth, googleProvider);
        const user = result.user;

        // 🔑 Get Firebase ID Token
        const token = await user.getIdToken();

        // ✅ Success popup
        alert(`Welcome ${user.displayName} ✅ Login Successful`);

        // 🔥 Send token to Flask to create session
        await fetch("/firebase-login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ idToken: token })
        });

        // ✅ Redirect to chatbot page
        window.location.href = "/index";

    } catch (error) {
        console.error(error);
        alert("Google login error: " + error.message);
    }
};
