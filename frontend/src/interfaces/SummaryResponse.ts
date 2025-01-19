export interface SummaryResponse {
  details: {
    email?: string[];
    full_name?: string[];
    tech_stacks: string[];
    experience: string[];
    languages_spoken: string[];
    phone_number: string[];
    institute: string[];
  };
  experience_level: string;
  skill_level: string;
}
