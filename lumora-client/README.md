# Overview – Onboarding Guide
   * [Lumora Client App – Onboarding Guide]()
     * [1. Request Access]()
     * [2. Clone the Repository]()
     * [3. Install Dependencies]()
     * [4. Configure Environment Variables]()
   * [How to Contribute]()

## Lumora Client App – Onboarding Guide

This is the **frontend client application** for Lumora, built with **Next.js**.
Follow the steps below to get properly onboarded with this project.

### 1. Request Access

Request a **contributor role** for this project.
Refer to the main **Lumora README** for details on how to do this.

### 2. Clone the Repository

```bash
git clone https://github.com/Itserge1/Lumora.git
```

### 3. Install Dependencies

Navigate into the project directory and install all required dependencies:

```bash
npm install
```

### 4. Configure Environment Variables

Create a `.env` file in the root of the **client folder**:

```
lumora-client/.env
```

Check `next.env.d.ts` for the required variables:
`lumora-client/next.env.d.ts`

```ts
declare namespace NodeJS {
    interface ProcessEnv {
        NEXT_PUBLIC_API_BASE_URL: string;
        // Add more variables here
    }
}
```

Example `.env` file:
`lumora-client/.env`

```env
NEXT_PUBLIC_API_BASE_URL="http://localhost:4000/"
// Add more variables here
```

## How to Contribute

1. **Sync with Main Branch**
   Always pull the latest changes from the `main` branch before starting new work:

   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create a New Branch**
   Create your own branch from `main`.
   Use the naming convention:

   ```
   firstName/short-description-of-work
   ```

   Example:

   ```
   john/add-navbar
   ```

3. **Make Your Changes**
   Add your code changes, commit them with clear messages, and push your branch:

   ```bash
   git push --set-upstream origin your/branch-name
   ```

4. **Open a Pull Request (PR)**

    * Go to the repository on GitHub.
    * Create a Pull Request from your branch into `main`.

5. **PR Workflow & Review**

    * Your PR must pass all automated checks/tests.
    * Each PR requires at least **one approval** before it can be merged into `main`.
