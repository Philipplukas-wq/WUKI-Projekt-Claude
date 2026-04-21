interface WissenshubCardProps {
  title: string;
  description: string;
  icon: string;
  badge?: string;
}

export default function WissenshubCard({ title, description, icon, badge }: WissenshubCardProps) {
  return (
    <div className="bg-white rounded-lg border border-[#e0e0e0] hover:border-[#4a5c3c] hover:shadow-md transition-all group p-6">
      <div className="flex items-start gap-4">
        <div className="w-10 h-10 rounded-lg bg-[#2d3142]/5 flex items-center justify-center text-xl flex-shrink-0 group-hover:bg-[#4a5c3c]/10 transition">
          {icon}
        </div>
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 mb-1">
            <h3 className="text-[#2d3142] font-semibold text-sm">{title}</h3>
            {badge && (
              <span className="text-[10px] bg-[#c8a84b]/15 text-[#8a6a1e] px-2 py-0.5 rounded-full font-medium">
                {badge}
              </span>
            )}
          </div>
          <p className="text-[#4a4e69] text-xs leading-relaxed">{description}</p>
        </div>
      </div>
    </div>
  );
}
