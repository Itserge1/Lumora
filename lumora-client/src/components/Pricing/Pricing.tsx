"use client";

import { ArrowRightIcon } from "@heroicons/react/16/solid";
import { ActionButton } from "../Button/ActionButton";

interface PricingGroup {
  title: string;
  features: Array<{ label: string }>;
}

const PricingCard = ({ title, features }: PricingGroup) => {
  return (
    <div className="border rounded-3xl border-primary-500 shadow-md max-w-lg p-10 w-sm">
      <h4 className="text-4xl text-center mt-4 font-extrabold">{title}</h4>
      <ul className="my-10">
        {features.map((feature) => (
          <li
            className="text-center text-lg mb-3 pb-3 border-b border-gray-700"
            key={feature.label}
          >
            {feature.label}
          </li>
        ))}
      </ul>
      <ActionButton size="lg" variant="primary" fullWidth>
        <span className="font-bold">Sign Up</span>
        <ArrowRightIcon className="size-5 ml-2" />
      </ActionButton>
    </div>
  );
};

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
      <h2 className="text-center text-5xl font-extrabold tracking-tighter mb-10">
        Choose Your Plan
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-3 justify-items-center max-w-10xl">
        {pricingGroups.map((group) => (
          <PricingCard
            key={group.title}
            title={group.title}
            features={group.features}
          />
        ))}
      </div>
    </section>
  );
};

export default Pricing;
