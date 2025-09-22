"use client"

import styles from './MainGoal.module.css'
import {useState} from "react";

const MainGoal = () => {
    const [activeIndex, setActiveIndex] = useState<number | null>(null)

    const toggleAccordion = (index:number) => {
        setActiveIndex(index === activeIndex? null: index);
        // console.log(`clicked ${index}`)
    }

    const items = [
        {
            title: "What is market news?",
            description: "Market news comprises reports, data, and analyses about global financial markets,including stock " +
                "movements, economic indicators, and corporate earnings, providing investors with information to make " +
                "informed decisions about their investments."
        },
        {
            title: "What is technical analysis?",
            description: "Technical analysis is the process of forecasting future financial market movements by studying " +
                "past market data, such as price and volume, to identify patterns and trends. It relies on the belief " +
                "that historical market action can predict future price activity, allowing traders to determine optimal " +
                "times for buying or selling securities."
        },
        {
            title: "What is fundamentals analysis?",
            description: "Fundamental analysis is an investment approach that seeks to determine a security intrinsic value " +
                "by examining a broad range of economic and financial factors, including a company financial statements, " +
                "industry trends, and the overall macroeconomic environment."
        }
    ]

    return (
        <section className={styles.maingoal}>
            <div className={`${styles["maingoal-title"]}`}>
                <h4>OUR PRODUCT</h4>
            </div>
            <div className={`${styles["maingoal-wrapper"]}`}>
                <div className={`${styles["accordion"]} ${styles["container"]}`}>
                    <div className={`${styles["accordion__container"]}`}>
                        {items.map((item, i) => (
                            <div key={i} className={`${styles["accordion__item"]}`} onClick={() => toggleAccordion(i)}>
                                <header className={`${styles["accordion__header"]}`}>
                                    <h3 className={`${styles["accordion__title"]} ${i === activeIndex ? styles["accordion__title-heavy"] : ""}`}>{item.title}</h3>
                                    <svg xmlns="http://www.w3.org/2000/svg"
                                         fill="none"
                                         viewBox="0 0 24 24"
                                         strokeWidth="1.5"
                                         stroke="currentColor"
                                         className={`size-6 ${styles["accordion__icon"]} ${i === activeIndex ? styles["accordion__icon--rotated"] : ""}`}>
                                        <path strokeLinecap="round" strokeLinejoin="round"
                                              d="m19.5 8.25-7.5 7.5-7.5-7.5"/>
                                    </svg>
                                </header>

                                <div className={`${styles["accordion__content"]} ${i === activeIndex? styles["accordion-open"]:""}`}>
                                    <p className={`${styles["accordion__description"]}`}>{item.description}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>


        </section>
    )
}

export default MainGoal;