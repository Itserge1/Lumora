"use client"

import styles from './NavBar.module.css'
import Button from "@/components/Button/Button";
import {useState} from "react";

const NavBar = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleNavbar = () => {
        setIsOpen(prev => !prev);
    }

    return (
        <section className={`${styles.navbar}`}>
            <div className={styles["navbar-logo"]}>LOGO</div>

            <div className={`${styles["navbar-toggle"]} ${ isOpen ? styles["active"] : ''}`}>
                <div className={styles["navbar-close"]} >
                    <svg onClick={toggleNavbar} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5"
                         stroke="currentColor" className="size-6">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M6 18 18 6M6 6l12 12"/>
                    </svg>
                </div>
                <div className={styles["navbar-toggle-links"]}>
                    <ul className={styles["navbar-links"]}>
                        <li><a href={'/'}>Home</a></li>
                        <li><a href={'/'}>Product</a></li>
                        <li><a href={'/'}>Pricing</a></li>
                        <li><a href={'/'}>Solution</a></li>
                    </ul>
                </div>
                <div className={styles["navbar-toggle-button"]}>
                    <Button
                        size="custom"
                        customStyles={{
                            '--button-min-width': '170px',
                            '--button-text-size': '1.3rem',
                            '--button-padding-x': '1rem',
                            '--button-padding-y': '.5rem',
                            '--button-svg-icon-width': '2rem',
                            '--button-svg-icon-height': '2rem',
                        }}
                    >
                        Sign Up
                    </Button>
                </div>
            </div>

            <div className={styles["navbar-center"]}>
                <ul className={styles["navbar-links"]}>
                    <li><a href={'/'}>Home</a></li>
                    <li><a href={'/'}>Product</a></li>
                    <li><a href={'/'}>Pricing</a></li>
                    <li><a href={'/'}>Solution</a></li>
                </ul>
            </div>
            <div className={styles["navbar-button"]}>
                <Button />
            </div>

            <div className={styles["navbar-hamburger-menu"]}>
                <svg onClick={toggleNavbar} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5"
                     stroke="currentColor" className="size-6">
                    <path strokeLinecap="round" strokeLinejoin="round"
                          d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
                </svg>
            </div>
        </section>
    )
}

export default NavBar;