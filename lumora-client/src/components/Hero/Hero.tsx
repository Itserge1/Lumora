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
                            <p>Hero Section 1</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <p>Hero Section 2</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <h3>Track What moves the Market?</h3>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <p>Hero Section 4</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <p>Hero Section 5</p>
                        </div>
                    </SwiperSlide>

                    <SwiperSlide>
                        <div className={`${styles['slide-content']}`}>
                            <p>Hero Section 6</p>
                        </div>
                    </SwiperSlide>
                </Swiper>
            </div>
        </section>
    )
}

export default Hero;