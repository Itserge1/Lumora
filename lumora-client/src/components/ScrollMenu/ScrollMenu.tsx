"use client"

import styles from "./ScrollMenu.module.css";
import {useState, useRef, useEffect} from "react";

// COMPONENTS
import News from "@/components/News/News";

const ScrollMenu = () => {
    // SCROLL MENU
    const [activeTab, setActiveTab] = useState('news');
    const headers = [
        "news",
        "earning",
        "sentiment",
        "others",
    ]

    const duplicateHeaders = [...headers, ...headers, ...headers]
    const scrollRef = useRef<HTMLDivElement>(null)

    useEffect(() => {
        const scrollContainer = scrollRef.current
        if (!scrollContainer) return;

        // Handle scroll
        const handleScroll = () => {
            const { scrollLeft, scrollWidth} = scrollContainer;

            const singleSetWidth = scrollWidth / 3;
            const scrollRepeat = (singleSetWidth * 2)

            // reset to the initial spot when reaching the end of the list
            if (scrollLeft >= scrollRepeat){
                scrollContainer.scrollLeft = singleSetWidth;
            }

            // reset to the initial spot when reaching the start of the list
            else if (scrollLeft <= 0){
                scrollContainer.scrollLeft = singleSetWidth;
            }
        }

        // Add scroll event and Set the starting point at the middle of the list
        scrollContainer.addEventListener("scroll", handleScroll)
        scrollContainer.scrollLeft = scrollContainer.scrollWidth / 3;

        // CLEAN UP: remove event listener on Unmount & rerender
        return () => scrollContainer.removeEventListener("scroll", handleScroll)
    }, []);


    return (
        <section>
            <div className={styles["scrollMenu__container"]}>
                {/*================= SCROLL BAR MENU =================*/}
                <div
                    className={styles["scrollMenu__toggle"]}
                    data-active={activeTab}
                    ref={scrollRef}
                >
                    {duplicateHeaders.map((header, index) => (
                        <span key={index}
                              className={activeTab === header ? styles.active : ''}
                              onClick={() => setActiveTab(header)}
                        >
                        {header}
                        </span>
                    ))}
                </div>

                {/*================= MENU CONTENT =================*/}
                <div className={styles["scrollMenu__content"]}>
                    {activeTab === 'news' && (
                        <div className={styles["tab__content"]} key="news">
                            <News/>
                            <News/>
                            <News/>
                            <News/>
                            <News/>
                        </div>
                    )}
                    {activeTab === 'earning' && (
                        <div className={styles["tab__content"]} key="earning">
                            Earning content here
                        </div>
                    )}
                    {activeTab === 'sentiment' && (
                        <div className={styles["tab__content"]} key="sentiment">
                            Sentiment content here
                        </div>
                    )}

                    {activeTab === 'others' && (
                        <div className={styles["tab__content"]} key="others">
                            others content here
                        </div>
                    )}
                </div>
            </div>
        </section>
    )
}

export default ScrollMenu;
