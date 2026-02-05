"use client"

import styles from './HomePage.module.css'

import {useEffect, useRef, useState} from "react";
import {
    createChart,
    IChartApi,
    AreaSeries,
    // BarSeries,
    // BaselineSeries,
    CandlestickSeries,
    HistogramSeries,
    UTCTimestamp,
    ColorType
} from 'lightweight-charts';

const Home = () => {
    const firstContainer = useRef<HTMLDivElement>(null);
    const firstChartRef = useRef<IChartApi>(null);

    useEffect(() => {
        // Create a chart when the component mounts
        if (firstContainer.current && !firstChartRef.current) {
            // create a chart
            const chartOptions = {
                width: firstContainer.current.clientWidth,
                height: firstContainer.current.clientHeight,
                autosize: true,
                layout: {
                    textColor: 'white',
                    background: {type: ColorType.Solid, color: '#111827'}
                },
            };
            firstChartRef.current = createChart(firstContainer.current, chartOptions);

            // Add area series to the chart
            const areaSeries = firstChartRef.current.addSeries(AreaSeries, {
                lineColor: '#2962FF', topColor: '#2962FF',
                bottomColor: 'rgba(41, 98, 255, 0.28)',
            });
            const areaData = [
                {time: '2018-12-22', value: 32.51},
                {time: '2018-12-23', value: 31.11},
                {time: '2018-12-24', value: 27.02},
                {time: '2018-12-25', value: 27.32},
                {time: '2018-12-26', value: 25.17},
                {time: '2018-12-27', value: 28.89},
                {time: '2018-12-28', value: 25.46},
                {time: '2018-12-29', value: 23.92},
                {time: '2018-12-30', value: 22.68},
                {time: '2018-12-31', value: 22.67},
            ];
            areaSeries.setData(areaData);

            // Add candlestick series to the chart
            const candlestickSeries = firstChartRef.current.addSeries(CandlestickSeries, {
                upColor: '#26a69a', downColor: '#ef5350', borderVisible: false,
                wickUpColor: '#26a69a', wickDownColor: '#ef5350',
            });
            const candlestickData = [
                {time: '2018-12-22', open: 75.16, high: 82.84, low: 36.16, close: 45.72},
                {time: '2018-12-23', open: 45.12, high: 53.90, low: 45.12, close: 48.09},
                {time: '2018-12-24', open: 60.71, high: 60.71, low: 53.39, close: 59.29},
                {time: '2018-12-25', open: 68.26, high: 68.26, low: 59.04, close: 60.50},
                {time: '2018-12-26', open: 67.71, high: 105.85, low: 66.67, close: 91.04},
                {time: '2018-12-27', open: 91.04, high: 121.40, low: 82.70, close: 111.40},
                {time: '2018-12-28', open: 111.51, high: 142.83, low: 103.34, close: 131.25},
                {time: '2018-12-29', open: 131.33, high: 151.17, low: 77.68, close: 96.43},
                {time: '2018-12-30', open: 106.33, high: 110.20, low: 90.39, close: 98.10},
                {time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 111.26},
            ]
            candlestickSeries.setData(candlestickData);

            // Add histogram series to the chart
            const histogramSeries = firstChartRef.current.addSeries(HistogramSeries, {color: '#26a69a'});
            const histogramData = [
                {value: 1, time: 1642425322 as UTCTimestamp},
                {value: 8, time: 1642511722 as UTCTimestamp},
                {value: 10, time: 1642598122 as UTCTimestamp},
                {value: 20, time: 1642684522 as UTCTimestamp},
                {value: 3, time: 1642770922 as UTCTimestamp, color: 'red'},
                {value: 43, time: 1642857322 as UTCTimestamp},
                {value: 41, time: 1642943722 as UTCTimestamp, color: 'red'},
                {value: 43, time: 1643030122 as UTCTimestamp},
                {value: 56, time: 1643116522 as UTCTimestamp},
                {value: 46, time: 1643202922 as UTCTimestamp, color: 'red'}
            ];
            histogramSeries.setData(histogramData);

            // Fit the chart to show all data points
            firstChartRef.current.timeScale().fitContent();
        }


        // Cleanup function to remove charts when the component unmounts
        return () => {
            if (firstChartRef.current) {
                firstChartRef.current.remove()
                firstChartRef.current = null
            }
        }
    }, []);

    const [activeTab, setActiveTab] = useState('news');
    return (
        <section className={styles.homePage}>
            <div className={styles["chart__container"]} ref={firstContainer}/>
            <div className={styles["financialInfos__container"]}>
                <div
                    className={styles["financialInfos__container__toggle"]}
                    data-active={activeTab}
                >
                    <span
                        className={activeTab === 'news' ? styles.active : ''}
                        onClick={() => setActiveTab('news')}
                    >
                        News
                    </span>

                    <span
                        className={activeTab === 'earning' ? styles.active : ''}
                        onClick={() => setActiveTab('earning')}
                    >
                        Earning
                    </span>

                    <span
                        className={activeTab === 'sentiment' ? styles.active : ''}
                        onClick={() => setActiveTab('sentiment')}
                    >
                        Sentiment
                    </span>
                </div>

                {/*<div className={styles["financialInfos__container__content"]}>*/}
                {/*    <div*/}
                {/*        className={styles["content__slider"]}*/}
                {/*        data-active={activeTab}*/}
                {/*    >*/}
                {/*        <div className={styles["content__slide"]}>News content here</div>*/}
                {/*        <div className={styles["content__slide"]}>Earning content here</div>*/}
                {/*        <div className={styles["content__slide"]}>Sentiment content here</div>*/}
                {/*    </div>*/}
                {/*</div>*/}

                <div className={styles["financialInfos__container__content"]}>
                    {activeTab === 'news' && (
                        <div className={styles["tab__content"]} key="news">
                            News content here
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
                </div>
            </div>
        </section>
    )
}

export default Home;