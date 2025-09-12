"use client"; // Treat this as a client components

import styles from "./HomePage.module.css";
import Hero from "@/components/Hero/Hero";
import NewsSource from "@/components/NewsSource/NewsSource";
import MainGoal from "@/components/MainGoal/MainGoal";
import WatchList from "@/components/WatchList/WatchList";
import Pricing from "@/components/Pricing/Pricing";
import Footer from "@/components/Footer/Footer";

const HomePage = () => {
    return (
        <section className={`${styles.homepage}`}>
            <Hero/>
            <NewsSource/>
            <MainGoal/>
            <WatchList/>
            <Pricing/>
            <Footer/>
        </section>
    );
};

export default HomePage;