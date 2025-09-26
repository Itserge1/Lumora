"use client"

import {Swiper, SwiperSlide} from "swiper/react";
import {Pagination, EffectCoverflow, Keyboard, Autoplay} from "swiper/modules";

import styles from './Hero.module.css'
import 'swiper/css';
import 'swiper/css/effect-coverflow';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

interface SwiperSlideProps {
    title: string,
    description: string,
}

const Hero = () => {
    const AllSwiperSlides: SwiperSlideProps[] = [
        {
            title: "Stock News Summaries",
            description: "Get bite-sized summaries of the latest stock news in seconds"
        },
        {
            title: "Market Movers Explained",
            description: "Understand why your favorite stock is up 📈 or down 📉 today."
        },
        {
            title: "Earnings Call Highlight",
            description: "Cut through transcripts with concise takeaways that matter"
        },
        {
            title: "Sector & Industry Trends",
            description: "Spot which sectors are heating up or cooling off."
        },
        {
            title: "Ticker-Based Feeds",
            description: "Follow the news that actually matters for your watchlist"
        },
        {
            title: "Sentiment Insights",
            description: "See if the news is bullish 🐂 or bearish 🐻 at a glance."
        }
    ]
    return (
        <section className={styles.hero}>
            <div className={`${styles["swiper-container"]}`}>
                <Swiper
                    effect="coverflow"
                    grabCursor={true}
                    centeredSlides={true}
                    slidesPerView="auto"
                    initialSlide={2}
                    loop={true}
                    autoplay={{
                        delay: 3000, // 3 seconds before auto swipe
                        disableOnInteraction: false, // keep autoplay even after user interacts
                    }}
                    keyboard={{enabled: true}}
                    mousewheel={{thresholdDelta: 70}}
                    coverflowEffect={{
                        rotate: 0,
                        stretch: 0,
                        depth: 100,
                        modifier: 4,
                        slideShadows: true,
                    }}
                    breakpoints={{
                        768: {slidesPerView: 2},
                        1024: {slidesPerView: 1.5},
                        1280: {slidesPerView: 1.7},
                    }}
                    pagination={{clickable: true}}
                    modules={[EffectCoverflow, Pagination, Keyboard, Autoplay]}
                    className="swiper"
                >
                    {AllSwiperSlides.map((slide, i) => (
                        <SwiperSlide key={i}>
                            <div className={`${styles['slide-content']}`}>
                                <h3>{slide.title}</h3>
                                <p>{slide.description}</p>
                            </div>
                        </SwiperSlide>
                    ))}
                </Swiper>
            </div>
        </section>
    )
}

export default Hero;