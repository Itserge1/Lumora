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
    <section className="bg-gray-800 text-white py-10 px-25">
      <h2 className="text-center text-5xl mb-10">Choose Your Plan</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 justify-items-center">
        {pricingGroups.map((group) => (
          <div
            key={group.title}
            className="border rounded-lg shadow-md max-w-lg p-6 w-sm"
          >
            <h4 className="text-4xl text-center my-4">{group.title}</h4>
            <ul className="mt-4">
              {group.features.map((feature) => (
                <li className="text-center text-lg mb-3" key={feature.label}>
                  {feature.label}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Pricing;
