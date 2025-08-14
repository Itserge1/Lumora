"use client"; // Treat this as a client component

import styles from "./HomePage.module.css";

const HomePage = () => {
  return (
    <section className={`${styles.homepage} ${styles["homepage-border"]} ${styles["homepage__text"]}`}>
      <p>Hello from Home Page test</p>
    </section>
  );
};

export default HomePage;