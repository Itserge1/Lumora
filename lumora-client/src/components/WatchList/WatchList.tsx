"use client"

import styles from './WatchList.module.css'
import clsx from 'clsx'
import StockTickerCart from "@/components/StockTickerCart/StockTickerCart";

interface stockTicker{
    name: string,
    percent: number
}

const WatchList = () => {
    const allTicker: stockTicker[] = [
        {name: "TSLA", percent: -10.89},
        {name: "NVDA", percent: 3.89},
        {name: "SPY", percent: 1.89},
        {name: "PLTR", percent: 2.89},
        {name: "AAPL", percent: -0.07},
        {name: "MSFT", percent: 0.89},
    ]

    return (
        <section className={styles.watchlist}>
            <div className={clsx(styles["watchlist__container"])}>
                <div className={clsx(styles["watchlist__cart"])}>
                    <div className={clsx(styles["watchlist__cart__top"])}>
                        <h4>CREATE YOUR WATCHLIST</h4>
                        <input
                            className={clsx(styles["watchlist__cart__searchbar"])}
                            type="search"
                            id="search_ticker"
                            name="search_ticker"
                            placeholder="Search stock ticker to add to your watchlist"
                        />
                    </div>
                    <div className={clsx(styles["watchlist__cart__bottom"])}>
                        {allTicker.map((item) => (
                            <StockTickerCart key={item.name} name={item.name} percent={item.percent}/>
                        ))}
                    </div>
                </div>
            </div>
        </section>
    )
}

export default WatchList