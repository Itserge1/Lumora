"use client"

import {Swiper, SwiperSlide} from "swiper/react";
import {Pagination, EffectCoverflow, Keyboard, Autoplay} from "swiper/modules";

import styles from './Hero.module.css'
import 'swiper/css';
import 'swiper/css/effect-coverflow';
import 'swiper/css/navigation';
import 'swiper/css/pagination';


const Hero = () => {
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
                        // 560: {slidesPerView: 2.5},
                        768: {slidesPerView: 2},
                        1024: {slidesPerView: 1.5},
                        1280: {slidesPerView: 1.7},
                    }}
                    pagination={{clickable: true}}
                    // modules={[EffectCoverflow, Pagination, Keyboard, Mousewheel]}
                    modules={[EffectCoverflow, Pagination, Keyboard, Autoplay]}
                    className="swiper"
                >
                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <h3>Stock News Summaries</h3>
                            <p>Get bite-sized summaries of the latest stock news in seconds</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <h3>Market Movers Explained</h3>
                            <p>Understand why your favorite stock is up 📈 or down 📉 today.</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <h3>Earnings Call Highlights</h3>
                            <p>Cut through transcripts with concise takeaways that matter</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <h3>Sector & Industry Trends</h3>
                            <p>Spot which sectors are heating up—or cooling off.</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <h3>Ticker-Based Feeds</h3>
                            <p>Follow the news that actually matters for your watchlist</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <h3>Sentiment Insights</h3>
                            <p>See if the news is bullish 🐂 or bearish 🐻 at a glance.</p>
                        </div>
                    </SwiperSlide>
                </Swiper>
            </div>
        </section>
    )
}

export default Hero;