"use client";

import { ArrowRightIcon } from "@heroicons/react/16/solid";
import { ActionButton } from "../Button/ActionButton";

interface PricingGroup {
  title: string;
  features: Array<{ label: string }>;
  button: string;
}

const PricingCard = ({ title, features, button }: PricingGroup) => {
  return (
    <div className="border rounded-3xl border-primary-500 shadow-md mb-6 sm:mb-8 md:mb-10 lg:mb-10 p-10 md:p-15 lg:p-10 w-full flex flex-col max-w-lg">
      <h4 className="text-4xl text-center font-extrabold">{title}</h4>
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
      <ActionButton size="lg" variant="primary" className="mt-auto" fullWidth>
        <span className="font-bold">{button}</span>
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
      button: "Get Started",
    },
    {
      title: "Premium",
      features: [
        { label: "Unlimited watchlists" },
        { label: "Fundamental analysis" },
        { label: "Technical analysis" },
        { label: "Retail & Suit Sentiment" },
      ],
      button: "Start Free Trial",
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
      button: "Start Free Trial",
    },
  ];

  return (
    <section className="py-10 px-2 lg:px-10 xl:px-25 mx-6 sm:mx-10 md:mx-0">
      <h2 className="text-center text-5xl font-extrabold tracking-tighter mb-10">
        Choose Your Plan
      </h2>
      <div className="grid grid-cols-1 lg:grid-cols-3 justify-items-center max-w-10xl lg:gap-5 xl:gap-10">
        {pricingGroups.map((group) => (
          <PricingCard
            key={group.title}
            title={group.title}
            features={group.features}
            button={group.button}
          />
        ))}
      </div>
    </section>
  );
};

export default Pricing;
