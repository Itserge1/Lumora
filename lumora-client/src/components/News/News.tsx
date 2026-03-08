"use client"

import styles from "./News.module.css";
import clsx from "clsx";

const News = () => {
    return(
        <section>
            <div className={clsx(styles.news__container)}>
                <div className={clsx(styles.news__source)}>
                    <div className={clsx(styles.news_logo)}>Logo</div>
                    <div className={clsx(styles.news__source__right)}>
                        <span >BULLISH</span>
                        <span className={clsx(styles.news_logo)}>5h</span>
                    </div>
                </div>
                <div className={clsx(styles.news__title)}>
                    <p>
                        Apple Reports Record Q4 Revenue, Beats Analyst Forecasts by Wide
                    </p>
                </div>
                <div className={clsx(styles.news__content)}>
                    <p>
                        iPhone sales surge 18% YoY as emerging markets drive unexpected demand, pushing revenue to $123.9B.
                    </p>
                </div>
                <div className={clsx(styles.news__bottom)}>
                    <div className={clsx(styles.news__relevance)}>
                        Relevance
                        <div className={clsx(styles.news__relevance_circle_group)}>
                            <span className={clsx(styles.news__relevance_circle, styles.circle_active)}></span>
                            <span className={clsx(styles.news__relevance_circle, styles.circle_active)}></span>
                            <span className={clsx(styles.news__relevance_circle, styles.circle_active)}></span>
                            <span className={clsx(styles.news__relevance_circle)}></span>
                            <span className={clsx(styles.news__relevance_circle)}></span>
                        </div>
                    </div>
                    <span className={clsx(styles.news__bottom__read)}>
                        read
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                             stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"
                             className="lucide lucide-chevrons-right-icon lucide-chevrons-right">
                            <path d="m6 17 5-5-5-5"/>
                            <path d="m13 17 5-5-5-5"/>
                        </svg>
                    </span>
                </div>
            </div>
        </section>
    )
}

export default News;
