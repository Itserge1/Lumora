"use client"; // Treat this as a client components

import styles from "./HomePage.module.css";
import NavBar from "@/components/NavBar/NavBar";

const HomePage = () => {
    return (
        <section className={`${styles.homepage}`}>
            <NavBar/>
        </section>
    );
};

export default HomePage;