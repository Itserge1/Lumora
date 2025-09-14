"use client";

import styles from "./Footer.module.css";
import type { ReactNode } from "react";

interface FooterLinkProps {
  href: string;
  children: ReactNode;
}

function FooterLink({ href, children }: FooterLinkProps) {
  return (
    <li>
      <a
        href={href}
        className="text-gray-300 hover:text-white transition-colors"
      >
        {children}
      </a>
    </li>
  );
}

interface LinkGroup {
  title: string;
  links: Array<{ href: string; label: string }>;
}

function Footer() {
  const linkGroups: LinkGroup[] = [
    {
      title: "Product",
      links: [
        { href: "#", label: "API" },
        { href: "#", label: "Features" },
        { href: "#", label: "Pricing" },
      ],
    },
    {
      title: "Company",
      links: [
        { href: "#", label: "About Us" },
        { href: "#", label: "Blog" },
        { href: "#", label: "Contact" },
      ],
    },
    {
      title: "Legal",
      links: [
        { href: "#", label: "Privacy Policy" },
        { href: "#", label: "Terms of Service " },
      ],
    },
  ];

  return (
    <footer className="bg-gray-800 text-white py-12">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <h3 className="text-xl font-bold">Lumora</h3>
            </div>
            <p className="text-gray-300">
              Intelligent stock news and insights for modern investors.
            </p>
          </div>

          {linkGroups.map((group) => (
            <div key={group.title}>
              <h4 className="font-semibold mb-4">{group.title}</h4>
              <ul className="space-y-2">
                {group.links.map((link) => (
                  <FooterLink key={link.label} href={link.href}>
                    {link.label}
                  </FooterLink>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-8 pt-8 border-t border-gray-700 text-center text-gray-400">
          <p>© {new Date().getFullYear()} Lumora. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
