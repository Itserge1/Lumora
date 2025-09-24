"use client";

import { ReactNode } from "react";

interface PricingGroup {
  title: string;
  features: Array<{ label: string }>;
}

const Pricing = () => {
  const pricingGroups: PricingGroup[] = [
    {
      title: "Free",
      features: [
        { label: "5 watchlist stocks" },
        { label: "Basic analytics" },
        { label: "Email alerts" },
        { label: "Daily news digest" },
      ],
    },
    {
      title: "Premium",
      features: [
        { label: "Unlimited watchlists" },
        { label: "Fundamental analysis" },
        { label: "Technical analysis" },
        { label: "Retail & Suit Sentiment" },
      ],
    },
    {
      title: "Gold",
      features: [
        { label: "Unlimited watchlists" },
        { label: "Fundamental analysis" },
        { label: "Technical analysis" },
        { label: "Retail & Suit Sentiment" },
        { label: "Short interest" },
      ],
    },
  ];

  return (
    <section className="bg-gray-800 text-white grid grid-cols-1 md:grid-cols-3 gap-8">
      {pricingGroups.map((group) => (
        <div key={group.title} className="border rounded-lg p-6 shadow-md">
          <h4>{group.title}</h4>
          <ul>
            {group.features.map((feature) => (
              <p key={feature.label}>{feature.label}</p>
            ))}
          </ul>
        </div>
      ))}
    </section>
  );
};

export default Pricing;
