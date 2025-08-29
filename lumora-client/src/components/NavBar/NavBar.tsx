"use client"

import  styles from './NavBar.module.css'
import Button from "@/components/Button/Button";

const NavBar = () => {
    return (
        <section className={`${styles.navbar}`}>
            <div className={styles["navbar-logo"]}>MAIN LOGO</div>
            <div className={styles["navbar-center"]}>
                <ul className={styles["navbar-links"]} >
                    <li><a href={'/'}>Home</a></li>
                    <li><a href={'/'}>Product</a></li>
                    <li><a href={'/'}>Pricing</a></li>
                    <li><a href={'/'}>Solution</a></li>
                </ul>
            </div>
            <div className={styles["navbar-button"]}>
                <Button />
            </div>
        </section>
    )
}

export default NavBar;