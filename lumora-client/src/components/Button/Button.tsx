import styles from './Button.module.css'

interface ButtonCSSVars {
    '--button-min-width'?: string;
    '--button-text-size'?: string;
    '--button-padding-x'?: string;
    '--button-padding-y'?: string;
    '--button-svg-icon-width'?: string
    '--button-svg-icon-height'?: string
}

interface ButtonProps {
    size?: 'small' | 'medium' | 'large' | 'custom';
    children?: React.ReactNode;
    customStyles?: React.CSSProperties & ButtonCSSVars;
}

const Button: React.FC<ButtonProps> = ({ size = 'medium', children = 'Sign up', customStyles }) => {
    return(
        <section>
            <a href={"/"} className={`${styles.button} ${size ? styles[size] : ''}`} style={customStyles} >
                <span className={`${styles['button-text']}`}>
                    {children}
                </span>
                <span className={`${styles["button-icon"]}`}>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" className="size-4">
                        <path fillRule="evenodd"
                              d="M2 8c0 .414.336.75.75.75h8.69l-1.22 1.22a.75.75 0 1 0 1.06 1.06l2.5-2.5a.75.75 0 0 0 0-1.06l-2.5-2.5a.75.75 0 1 0-1.06 1.06l1.22 1.22H2.75A.75.75 0 0 0 2 8Z"
                              clipRule="evenodd"/>
                    </svg>
                </span>
            </a>
        </section>
    )
}

export default Button;