"use client"

import styles from './NewsSource.module.css'

import Image from "next/image";

const NewsSource = () => {
    return(
        <section className={styles.newssource}>
            <h4>NEWS PARTNERS</h4>
            <div className={`${styles["newssource-icons-groups"]}`}>
                <div className={`${styles["newssource-icon_yahoo_finance"]}`}>
                    <Image
                        src="/yahoo_finance.svg"
                        alt="cnbc icons"
                        width={150}
                        height={150}
                    />
                </div>

                <div className={`${styles["newssource-icon_cnbc"]}`}>
                    <Image
                        src="/icons8-nbc-color/icons8-nbc-480.png"
                        alt="cnbc icons"
                        width={50}
                        height={50}
                    /><span>CNBC</span>
                </div>

                <div>
                    <Image
                        src="/bloomberg.svg"
                        alt="bloomberg icon"
                        width={100}
                        height={100}
                    />
                </div>

                <div>
                    <Image
                        src="/The_Wall_Street_Journal.svg"
                        alt="The Wall Street Journal icon"
                        width={50}
                        height={50}
                    />
                </div>
            </div>
        </section>
    )
}

export default NewsSource;