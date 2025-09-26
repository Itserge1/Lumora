"use client";
import styles from "./StockTickerCart.module.css";
import clsx from "clsx";

interface StockTickerCartProps {
    name: string;
    percent: number;
}

const StockTickerCart = ({ name, percent } : StockTickerCartProps) => {
    const isPositive = percent >= 0;
    const formattedPercent = `${isPositive ? "+" : ""}${percent.toFixed(2)}%`;

    return (
        <section className={styles.tickercart}>
            <span>{name}</span>
            <span
                className={clsx(
                    styles.tickercart__percent,
                    isPositive ? styles["tickercart__percent-up"] : styles["tickercart__percent-down"]
                )}
            >
        {formattedPercent}
      </span>
        </section>
    );
};

export default StockTickerCart;
