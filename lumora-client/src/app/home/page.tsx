"use client"

import styles from './HomePage.module.css';
import clsx from "clsx";

import ScrollMenu from "@/components/ScrollMenu/ScrollMenu";
import StockChart from "@/components/StockChart/StockChart";

const Home = () => {
    return (
        <section className={clsx(
            styles.homePage,
        )}>
            <StockChart />
            <ScrollMenu />
        </section>
    )
}

export default Home;