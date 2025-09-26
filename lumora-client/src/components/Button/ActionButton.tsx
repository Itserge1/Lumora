import type { ReactNode } from "react";

interface ButtonProps {
  children: ReactNode;
  variant?: "primary" | "secondary";
  size?: "sm" | "md" | "lg";
  className?: string;
  href?: string;
  disabled?: boolean;
  loading?: boolean;
  fullWidth?: boolean;
  onClick?: () => void;
}

export function ActionButton({
  children,
  variant = "primary",
  size = "md",
  className = "",
  href = "",
  disabled = false,
  loading = false,
  fullWidth = false,
  onClick,
}: ButtonProps) {
  const baseClasses = `inline-flex items-center justify-center font-medium rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 transition-colors ${className}`;

  const variantClasses = {
    primary:
      loading || disabled
        ? "bg-primary-300 cursor-not-allowed text-white"
        : "bg-primary-500 hover:bg-primary-600 text-white focus:ring-primary-500",
    secondary:
      "bg-white text-primary-500 border border-primary-500 hover:bg-gray-50 focus:ring-primary-500",
  };

  const sizeClasses = {
    sm: "px-3 py-1.5 text-sm",
    md: "px-4 py-2 text-sm",
    lg: "px-6 py-3 text-base",
  };

  const widthClasses = fullWidth ? "w-full" : "";

  const commonClasses = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${widthClasses} ${className}`;

  if (href) {
    return (
      <a href={href} className={commonClasses}>
        {children}
      </a>
    );
  }

  return (
    <button onClick={onClick} className={commonClasses}>
      {children}
    </button>
  );
}
