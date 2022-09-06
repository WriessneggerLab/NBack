# N-Back Task

Programmed for [0, 1, 2, 3]-back tasks. Lists are pre-randomized. Generated with `src/create_trials.py`. Currently, 20 trials are presented on every task. 12 task for every block. One single experimental block.
Every trial is about 60 seconds. Experiment lasts ~12 min. Designed that way to avoid XR motion sickness interruption of experiments.

12 Lists are generated for a 12 min experiment. 3 lists for each of the 4 "n" conditions. They are presented at random.

Stimuli can be changed from characters to words, sentences, numbers, emoticons, etc.

Relevant logs: 
- `resp_key_trial.rt` Trial response time.
- `resp_key_trial.corr` 1 if trial answered correctly, 0 otherwise.

Relevant LSL markers:
- `T{n}/{trial_list}` at the "pre" screen of every task.
- `{tg}/{x}` Not so relevant for now.

Based on Grimes 2008[[1](1)].

## References

[1]: Grimes, D., Tan, D. S., Hudson, S. E., Shenoy, P., & Rao, R. P. (2008, April). Feasibility and pragmatics of classifying working memory load with an electroencephalograph. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 835-844).
