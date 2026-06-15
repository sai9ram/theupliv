new_block = '''                <!-- RIGHT: Scroll-driven stacking cards -->
                <div class="w-full lg:w-[62%] relative" id="approach-scene">

                    <!-- DESKTOP: Sticky stage holds all 5 cards absolutely stacked -->
                    <!-- The proxy below creates the scroll travel space -->
                    <div id="approach-stage" class="hidden lg:block"
                         style="position:sticky;top:120px;height:540px;z-index:10;">

                        <!-- CARD 1 green — initially fully visible -->
                        <div class="approach-card" data-card="0"
                             style="position:absolute;inset:0;border-radius:20px;padding:36px 40px;overflow:hidden;
                                    border:1px solid rgba(197,235,217,0.4);background:rgba(197,235,217,0.03);
                                    box-shadow:0 0 60px 0 rgba(197,235,217,0.08);
                                    z-index:50;opacity:1;transform:scale(1) translateY(0);
                                    transition:transform .55s cubic-bezier(.4,0,.2,1),opacity .55s ease,border-color .3s ease;">
                            <div style="position:absolute;top:-40px;right:-40px;width:192px;height:192px;border-radius:9999px;filter:blur(64px);opacity:.2;background:#c5ebd9;pointer-events:none;"></div>
                            <div style="position:relative;z-index:10;height:100%;display:flex;flex-direction:column;gap:18px;">
                                <div style="display:flex;align-items:center;justify-content:space-between;">
                                    <div style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(197,235,217,0.1);border:1px solid rgba(197,235,217,0.2);">💬</div>
                                    <span class="font-mono font-black tracking-tight" style="font-size:60px;color:rgba(255,255,255,0.05);">01</span>
                                </div>
                                <div>
                                    <p class="font-body font-bold uppercase tracking-widest text-[#c5ebd9]" style="font-size:11px;margin-bottom:6px;">Client Discussions</p>
                                    <h3 class="font-heading font-extrabold text-white leading-tight" style="font-size:24px;margin-bottom:8px;">Understand project requirements and business goals.</h3>
                                    <p class="font-body text-white/55 leading-relaxed" style="font-size:14px;">Observe real client briefings from day one — learning how businesses identify needs, set expectations, and communicate before any project begins.</p>
                                </div>
                                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#c5ebd9;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Requirement Gathering</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#c5ebd9;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Business Communication</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#c5ebd9;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Client Relationship</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#c5ebd9;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Project Understanding</span></div>
                                </div>
                            </div>
                        </div>

                        <!-- CARD 2 purple — hidden below, slides up -->
                        <div class="approach-card" data-card="1"
                             style="position:absolute;inset:0;border-radius:20px;padding:36px 40px;overflow:hidden;
                                    border:1px solid rgba(129,140,248,0.1);background:rgba(255,255,255,0.02);
                                    z-index:40;opacity:0;transform:translateY(60px) scale(0.97);
                                    transition:transform .55s cubic-bezier(.4,0,.2,1),opacity .55s ease,border-color .3s ease;">
                            <div style="position:absolute;top:-40px;right:-40px;width:192px;height:192px;border-radius:9999px;filter:blur(64px);opacity:.2;background:#818cf8;pointer-events:none;"></div>
                            <div style="position:relative;z-index:10;height:100%;display:flex;flex-direction:column;gap:18px;">
                                <div style="display:flex;align-items:center;justify-content:space-between;">
                                    <div style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(129,140,248,0.1);border:1px solid rgba(129,140,248,0.2);">⚙️</div>
                                    <span class="font-mono font-black tracking-tight" style="font-size:60px;color:rgba(255,255,255,0.05);">02</span>
                                </div>
                                <div>
                                    <p class="font-body font-bold uppercase tracking-widest text-[#818cf8]" style="font-size:11px;margin-bottom:6px;">Industry Workflows</p>
                                    <h3 class="font-heading font-extrabold text-white leading-tight" style="font-size:24px;margin-bottom:8px;">Learn how teams collaborate and deliver results.</h3>
                                    <p class="font-body text-white/55 leading-relaxed" style="font-size:14px;">Exposure to how professional departments manage tasks, use agile processes, and coordinate across teams to deliver quality outcomes on time.</p>
                                </div>
                                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#818cf8;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Team Collaboration</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#818cf8;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Agile Workflows</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#818cf8;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Project Coordination</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#818cf8;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Task Management</span></div>
                                </div>
                            </div>
                        </div>

                        <!-- CARD 3 amber -->
                        <div class="approach-card" data-card="2"
                             style="position:absolute;inset:0;border-radius:20px;padding:36px 40px;overflow:hidden;
                                    border:1px solid rgba(245,158,11,0.1);background:rgba(255,255,255,0.02);
                                    z-index:30;opacity:0;transform:translateY(60px) scale(0.97);
                                    transition:transform .55s cubic-bezier(.4,0,.2,1),opacity .55s ease,border-color .3s ease;">
                            <div style="position:absolute;top:-40px;right:-40px;width:192px;height:192px;border-radius:9999px;filter:blur(64px);opacity:.2;background:#f59e0b;pointer-events:none;"></div>
                            <div style="position:relative;z-index:10;height:100%;display:flex;flex-direction:column;gap:18px;">
                                <div style="display:flex;align-items:center;justify-content:space-between;">
                                    <div style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.2);">📊</div>
                                    <span class="font-mono font-black tracking-tight" style="font-size:60px;color:rgba(255,255,255,0.05);">03</span>
                                </div>
                                <div>
                                    <p class="font-body font-bold uppercase tracking-widest text-[#f59e0b]" style="font-size:11px;margin-bottom:6px;">Strategic Planning</p>
                                    <h3 class="font-heading font-extrabold text-white leading-tight" style="font-size:24px;margin-bottom:8px;">Observe decision-making and execution processes.</h3>
                                    <p class="font-body text-white/55 leading-relaxed" style="font-size:14px;">Understand how businesses allocate resources, set goals, and create strategies that translate into real business growth and competitive advantage.</p>
                                </div>
                                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#f59e0b;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Business Thinking</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#f59e0b;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Planning Frameworks</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#f59e0b;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Goal Setting</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#f59e0b;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Execution Strategy</span></div>
                                </div>
                            </div>
                        </div>

                        <!-- CARD 4 teal -->
                        <div class="approach-card" data-card="3"
                             style="position:absolute;inset:0;border-radius:20px;padding:36px 40px;overflow:hidden;
                                    border:1px solid rgba(52,211,153,0.1);background:rgba(255,255,255,0.02);
                                    z-index:20;opacity:0;transform:translateY(60px) scale(0.97);
                                    transition:transform .55s cubic-bezier(.4,0,.2,1),opacity .55s ease,border-color .3s ease;">
                            <div style="position:absolute;top:-40px;right:-40px;width:192px;height:192px;border-radius:9999px;filter:blur(64px);opacity:.2;background:#34d399;pointer-events:none;"></div>
                            <div style="position:relative;z-index:10;height:100%;display:flex;flex-direction:column;gap:18px;">
                                <div style="display:flex;align-items:center;justify-content:space-between;">
                                    <div style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(52,211,153,0.1);border:1px solid rgba(52,211,153,0.2);">🤝</div>
                                    <span class="font-mono font-black tracking-tight" style="font-size:60px;color:rgba(255,255,255,0.05);">04</span>
                                </div>
                                <div>
                                    <p class="font-body font-bold uppercase tracking-widest text-[#34d399]" style="font-size:11px;margin-bottom:6px;">Professional Communication</p>
                                    <h3 class="font-heading font-extrabold text-white leading-tight" style="font-size:24px;margin-bottom:8px;">Develop workplace collaboration skills.</h3>
                                    <p class="font-body text-white/55 leading-relaxed" style="font-size:14px;">Build the soft skills employers look for — from effective emails and presentations to navigating team dynamics and professional etiquette.</p>
                                </div>
                                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#34d399;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Team Communication</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#34d399;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Client Interaction</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#34d399;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Presentation Skills</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#34d399;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Workplace Etiquette</span></div>
                                </div>
                            </div>
                        </div>

                        <!-- CARD 5 red -->
                        <div class="approach-card" data-card="4"
                             style="position:absolute;inset:0;border-radius:20px;padding:36px 40px;overflow:hidden;
                                    border:1px solid rgba(248,113,113,0.1);background:rgba(255,255,255,0.02);
                                    z-index:10;opacity:0;transform:translateY(60px) scale(0.97);
                                    transition:transform .55s cubic-bezier(.4,0,.2,1),opacity .55s ease,border-color .3s ease;">
                            <div style="position:absolute;top:-40px;right:-40px;width:192px;height:192px;border-radius:9999px;filter:blur(64px);opacity:.2;background:#f87171;pointer-events:none;"></div>
                            <div style="position:relative;z-index:10;height:100%;display:flex;flex-direction:column;gap:18px;">
                                <div style="display:flex;align-items:center;justify-content:space-between;">
                                    <div style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(248,113,113,0.1);border:1px solid rgba(248,113,113,0.2);">🚀</div>
                                    <span class="font-mono font-black tracking-tight" style="font-size:60px;color:rgba(255,255,255,0.05);">05</span>
                                </div>
                                <div>
                                    <p class="font-body font-bold uppercase tracking-widest text-[#f87171]" style="font-size:11px;margin-bottom:6px;">Business Problem Solving</p>
                                    <h3 class="font-heading font-extrabold text-white leading-tight" style="font-size:24px;margin-bottom:8px;">Understand how companies tackle real challenges.</h3>
                                    <p class="font-body text-white/55 leading-relaxed" style="font-size:14px;">Develop critical thinking by watching how real businesses identify problems, evaluate solutions, and execute strategies to achieve measurable results.</p>
                                </div>
                                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#f87171;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Critical Thinking</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#f87171;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Analytical Skills</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#f87171;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Decision Making</span></div>
                                    <div style="display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"><span style="color:#f87171;font-size:12px;">✓</span><span class="font-heading font-bold text-white/80" style="font-size:12px;">Solution Development</span></div>
                                </div>
                            </div>
                        </div>

                    </div><!-- /approach-stage -->

                    <!-- Scroll proxy: 5 cards x 80vh — keeps stage sticky while scrolling (desktop only) -->
                    <div id="approach-proxy" class="hidden lg:block" style="height:400vh;"></div>

                    <!-- MOBILE: simple stacked cards -->
                    <div class="lg:hidden space-y-5 pb-10">
                        <div class="rounded-[18px] p-6 border" style="background:rgba(197,235,217,0.04);border-color:rgba(197,235,217,0.3);"><p class="font-body text-xs font-bold uppercase tracking-widest text-[#c5ebd9] mb-2">💬 Client Discussions</p><h3 class="font-heading text-lg font-extrabold text-white mb-2">Understand project requirements and business goals.</h3><p class="font-body text-white/55 text-sm leading-relaxed">Observe real client briefings from day one — how businesses identify needs and communicate before projects begin.</p></div>
                        <div class="rounded-[18px] p-6 border" style="background:rgba(129,140,248,0.04);border-color:rgba(129,140,248,0.3);"><p class="font-body text-xs font-bold uppercase tracking-widest text-[#818cf8] mb-2">⚙️ Industry Workflows</p><h3 class="font-heading text-lg font-extrabold text-white mb-2">Learn how teams collaborate and deliver results.</h3><p class="font-body text-white/55 text-sm leading-relaxed">How departments manage tasks and deliver quality outcomes using agile processes.</p></div>
                        <div class="rounded-[18px] p-6 border" style="background:rgba(245,158,11,0.04);border-color:rgba(245,158,11,0.3);"><p class="font-body text-xs font-bold uppercase tracking-widest text-[#f59e0b] mb-2">📊 Strategic Planning</p><h3 class="font-heading text-lg font-extrabold text-white mb-2">Observe decision-making and execution processes.</h3><p class="font-body text-white/55 text-sm leading-relaxed">How businesses allocate resources and create strategies for growth.</p></div>
                        <div class="rounded-[18px] p-6 border" style="background:rgba(52,211,153,0.04);border-color:rgba(52,211,153,0.3);"><p class="font-body text-xs font-bold uppercase tracking-widest text-[#34d399] mb-2">🤝 Professional Communication</p><h3 class="font-heading text-lg font-extrabold text-white mb-2">Develop workplace collaboration skills.</h3><p class="font-body text-white/55 text-sm leading-relaxed">From presentations to navigating team dynamics and workplace etiquette.</p></div>
                        <div class="rounded-[18px] p-6 border" style="background:rgba(248,113,113,0.04);border-color:rgba(248,113,113,0.3);"><p class="font-body text-xs font-bold uppercase tracking-widest text-[#f87171] mb-2">🚀 Business Problem Solving</p><h3 class="font-heading text-lg font-extrabold text-white mb-2">Understand how companies tackle real challenges.</h3><p class="font-body text-white/55 text-sm leading-relaxed">Critical thinking by watching how businesses identify problems and execute solutions.</p></div>
                    </div>

                </div><!-- /approach-scene -->
                <!-- end cards stack -->'''

with open('academy.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if '<!-- RIGHT: Scrollable Cards Stack -->' in line and start_idx is None:
        start_idx = i
    if '<!-- end cards stack -->' in line and start_idx is not None:
        end_idx = i
        break

if start_idx is None or end_idx is None:
    print(f'ERROR: markers not found. start={start_idx}, end={end_idx}')
else:
    new_lines = lines[:start_idx] + new_block.split('\n') + lines[end_idx+1:]
    with open('academy.html', 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    print(f'SUCCESS: replaced lines {start_idx+1}–{end_idx+1}. New total lines: {len(new_lines)}')
