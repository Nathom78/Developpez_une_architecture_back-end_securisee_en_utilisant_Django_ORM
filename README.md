# Developpez_une_architecture_back-end_securisee_en_utilisant_Django_ORM
[**Projet 12** du parcours OpenClassrooms Développeur d'application - Python](https://course.oc-static.com/projects/Python+FR/840+D%C3%A9veloppez+une+architecture+back-end+s%C3%A9curis%C3%A9e/Ancienne+Version-De%CC%81veloppez+une+architecture+back-end+se%CC%81curise%CC%81e+en+utilisant+Django+ORM.pdf)

[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOTIuODciIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAzOTIuODcgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxMTUuMzEiIGhlaWdodD0iMzUiIGZpbGw9IiNFQTQ1NjAiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxMTMuMzEiIHk9IjAiIHdpZHRoPSIyNzkuNTYiIGhlaWdodD0iMzUiIGZpbGw9IiNDMTNCM0EiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNjkgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTYuMTQgMTMuNDdMMTguNjAgMjAuMDFMMjEuMDYgMTMuNDdMMjIuOTcgMTMuNDdMMjIuOTcgMjJMMjEuNDkgMjJMMjEuNDkgMTkuMTlMMjEuNjQgMTUuNDNMMTkuMTIgMjJMMTguMDYgMjJMMTUuNTUgMTUuNDNMMTUuNjkgMTkuMTlMMTUuNjkgMjJaTTI4LjQ5IDIyTDI2Ljk1IDIyTDMwLjE3IDEzLjQ3TDMxLjUwIDEzLjQ3TDM0LjczIDIyTDMzLjE4IDIyTDMyLjQ5IDIwLjAxTDI5LjE4IDIwLjAxTDI4LjQ5IDIyWk0zMC44MyAxNS4yOEwyOS42MCAxOC44MkwzMi4wNyAxOC44MkwzMC44MyAxNS4yOFpNNDEuMTQgMjJMMzguNjkgMjJMMzguNjkgMTMuNDdMNDEuMjEgMTMuNDdRNDIuMzQgMTMuNDcgNDMuMjEgMTMuOTdRNDQuMDkgMTQuNDggNDQuNTcgMTUuNDBRNDUuMDUgMTYuMzMgNDUuMDUgMTcuNTJMNDUuMDUgMTcuNTJMNDUuMDUgMTcuOTVRNDUuMDUgMTkuMTYgNDQuNTcgMjAuMDhRNDQuMDggMjEuMDAgNDMuMTkgMjEuNTBRNDIuMzAgMjIgNDEuMTQgMjJMNDEuMTQgMjJaTTQwLjE3IDE0LjY2TDQwLjE3IDIwLjgyTDQxLjE0IDIwLjgyUTQyLjMwIDIwLjgyIDQyLjkzIDIwLjA5UTQzLjU1IDE5LjM2IDQzLjU2IDE3Ljk5TDQzLjU2IDE3Ljk5TDQzLjU2IDE3LjUyUTQzLjU2IDE2LjEzIDQyLjk2IDE1LjQwUTQyLjM1IDE0LjY2IDQxLjIxIDE0LjY2TDQxLjIxIDE0LjY2TDQwLjE3IDE0LjY2Wk01NS4wOSAyMkw0OS41MSAyMkw0OS41MSAxMy40N0w1NS4wNSAxMy40N0w1NS4wNSAxNC42Nkw1MS4wMCAxNC42Nkw1MS4wMCAxNy4wMkw1NC41MCAxNy4wMkw1NC41MCAxOC4xOUw1MS4wMCAxOC4xOUw1MS4wMCAyMC44Mkw1NS4wOSAyMC44Mkw1NS4wOSAyMlpNNjYuNjUgMjJMNjQuNjggMTMuNDdMNjYuMTUgMTMuNDdMNjcuNDcgMTkuODhMNjkuMTAgMTMuNDdMNzAuMzQgMTMuNDdMNzEuOTYgMTkuODlMNzMuMjcgMTMuNDdMNzQuNzQgMTMuNDdMNzIuNzcgMjJMNzEuMzUgMjJMNjkuNzMgMTUuNzdMNjguMDcgMjJMNjYuNjUgMjJaTTgwLjM4IDIyTDc4LjkwIDIyTDc4LjkwIDEzLjQ3TDgwLjM4IDEzLjQ3TDgwLjM4IDIyWk04Ni44NyAxNC42Nkw4NC4yMyAxNC42Nkw4NC4yMyAxMy40N0w5MS4wMCAxMy40N0w5MS4wMCAxNC42Nkw4OC4zNCAxNC42Nkw4OC4zNCAyMkw4Ni44NyAyMkw4Ni44NyAxNC42NlpNOTYuMjQgMjJMOTQuNzUgMjJMOTQuNzUgMTMuNDdMOTYuMjQgMTMuNDdMOTYuMjQgMTcuMDJMMTAwLjA1IDE3LjAyTDEwMC4wNSAxMy40N0wxMDEuNTMgMTMuNDdMMTAxLjUzIDIyTDEwMC4wNSAyMkwxMDAuMDUgMTguMjFMOTYuMjQgMTguMjFMOTYuMjQgMjJaIiBmaWxsPSIjRkZGRkZGIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTEzMS40NyAyMkwxMjcuNTAgMjJMMTI3LjUwIDEzLjYwTDEzMS40NyAxMy42MFExMzIuODUgMTMuNjAgMTMzLjkyIDE0LjEyUTEzNC45OSAxNC42MyAxMzUuNTggMTUuNThRMTM2LjE2IDE2LjUzIDEzNi4xNiAxNy44MEwxMzYuMTYgMTcuODBRMTM2LjE2IDE5LjA3IDEzNS41OCAyMC4wMlExMzQuOTkgMjAuOTcgMTMzLjkyIDIxLjQ4UTEzMi44NSAyMiAxMzEuNDcgMjJMMTMxLjQ3IDIyWk0xMjkuODggMTUuNTBMMTI5Ljg4IDIwLjEwTDEzMS4zOCAyMC4xMFExMzIuNDUgMjAuMTAgMTMzLjExIDE5LjQ5UTEzMy43NiAxOC44OCAxMzMuNzYgMTcuODBMMTMzLjc2IDE3LjgwUTEzMy43NiAxNi43MiAxMzMuMTEgMTYuMTFRMTMyLjQ1IDE1LjUwIDEzMS4zOCAxNS41MEwxMzEuMzggMTUuNTBMMTI5Ljg4IDE1LjUwWk0xMzkuODEgMjAuOTNMMTM5LjgxIDIwLjkzTDE0MS4xMSAxOS40MFExNDEuNzggMjAuMjcgMTQyLjU1IDIwLjI3TDE0Mi41NSAyMC4yN1ExNDIuNTYgMjAuMjcgMTQyLjU2IDIwLjI3TDE0Mi41NiAyMC4yN1ExNDMuMDggMjAuMjcgMTQzLjM1IDE5Ljk2UTE0My42MiAxOS42NSAxNDMuNjIgMTkuMDVMMTQzLjYyIDE5LjA1TDE0My42MiAxNS40NEwxNDAuNzIgMTUuNDRMMTQwLjcyIDEzLjYwTDE0NS45NyAxMy42MEwxNDUuOTcgMTguOTFRMTQ1Ljk3IDIwLjU0IDE0NS4xNSAyMS4zNlExNDQuMzMgMjIuMTcgMTQyLjczIDIyLjE3TDE0Mi43MyAyMi4xN1ExNDEuODEgMjIuMTcgMTQxLjA1IDIxLjg1UTE0MC4yOSAyMS41MyAxMzkuODEgMjAuOTNaTTE1Mi40OCAyMkwxNTAuMDUgMjJMMTUzLjc2IDEzLjYwTDE1Ni4xMCAxMy42MEwxNTkuODIgMjJMMTU3LjM1IDIyTDE1Ni42OSAyMC4zN0wxNTMuMTQgMjAuMzdMMTUyLjQ4IDIyWk0xNTQuOTEgMTUuOTNMMTUzLjgzIDE4LjYxTDE1NS45OSAxOC42MUwxNTQuOTEgMTUuOTNaTTE2Ni4zMCAyMkwxNjMuOTcgMjJMMTYzLjk3IDEzLjYwTDE2NS45MyAxMy42MEwxNjkuNjQgMTguMDdMMTY5LjY0IDEzLjYwTDE3MS45NiAxMy42MEwxNzEuOTYgMjJMMTcwLjAxIDIyTDE2Ni4zMCAxNy41MkwxNjYuMzAgMjJaTTE3Ni43MCAxNy44MEwxNzYuNzAgMTcuODBRMTc2LjcwIDE2LjU0IDE3Ny4zMCAxNS41NFExNzcuODkgMTQuNTUgMTc4Ljk2IDEzLjk5UTE4MC4wMyAxMy40MyAxODEuMzcgMTMuNDNMMTgxLjM3IDEzLjQzUTE4Mi41NSAxMy40MyAxODMuNDkgMTMuODNRMTg0LjQzIDE0LjIyIDE4NS4wNSAxNC45N0wxODUuMDUgMTQuOTdMMTgzLjU0IDE2LjMzUTE4Mi42OSAxNS40MCAxODEuNTIgMTUuNDBMMTgxLjUyIDE1LjQwUTE4MS41MCAxNS40MCAxODEuNTAgMTUuNDBMMTgxLjUwIDE1LjQwUTE4MC40MiAxNS40MCAxNzkuNzYgMTYuMDZRMTc5LjEwIDE2LjcxIDE3OS4xMCAxNy44MEwxNzkuMTAgMTcuODBRMTc5LjEwIDE4LjUwIDE3OS40MCAxOS4wNFExNzkuNzAgMTkuNTkgMTgwLjI0IDE5Ljg5UTE4MC43OCAyMC4yMCAxODEuNDcgMjAuMjBMMTgxLjQ3IDIwLjIwUTE4Mi4xNiAyMC4yMCAxODIuNzYgMTkuOTNMMTgyLjc2IDE5LjkzTDE4Mi43NiAxNy42MkwxODQuODYgMTcuNjJMMTg0Ljg2IDIxLjEwUTE4NC4xMyAyMS42MSAxODMuMjAgMjEuODlRMTgyLjI3IDIyLjE3IDE4MS4zMyAyMi4xN0wxODEuMzMgMjIuMTdRMTgwLjAxIDIyLjE3IDE3OC45NSAyMS42MVExNzcuODkgMjEuMDUgMTc3LjMwIDIwLjA1UTE3Ni43MCAxOS4wNiAxNzYuNzAgMTcuODBaTTE4OS40MiAxNy44MEwxODkuNDIgMTcuODBRMTg5LjQyIDE2LjU1IDE5MC4wMiAxNS41NVExOTAuNjMgMTQuNTYgMTkxLjY5IDE0LjAwUTE5Mi43NSAxMy40MyAxOTQuMDggMTMuNDNMMTk0LjA4IDEzLjQzUTE5NS40MSAxMy40MyAxOTYuNDggMTQuMDBRMTk3LjU0IDE0LjU2IDE5OC4xNSAxNS41NVExOTguNzUgMTYuNTUgMTk4Ljc1IDE3LjgwTDE5OC43NSAxNy44MFExOTguNzUgMTkuMDUgMTk4LjE1IDIwLjA0UTE5Ny41NCAyMS4wNCAxOTYuNDggMjEuNjBRMTk1LjQyIDIyLjE3IDE5NC4wOCAyMi4xN0wxOTQuMDggMjIuMTdRMTkyLjc1IDIyLjE3IDE5MS42OSAyMS42MFExOTAuNjMgMjEuMDQgMTkwLjAyIDIwLjA0UTE4OS40MiAxOS4wNSAxODkuNDIgMTcuODBaTTE5MS44MiAxNy44MEwxOTEuODIgMTcuODBRMTkxLjgyIDE4LjUxIDE5Mi4xMiAxOS4wNVExOTIuNDIgMTkuNjAgMTkyLjk0IDE5LjkwUTE5My40NSAyMC4yMCAxOTQuMDggMjAuMjBMMTk0LjA4IDIwLjIwUTE5NC43MiAyMC4yMCAxOTUuMjQgMTkuOTBRMTk1Ljc1IDE5LjYwIDE5Ni4wNSAxOS4wNVExOTYuMzUgMTguNTEgMTk2LjM1IDE3LjgwTDE5Ni4zNSAxNy44MFExOTYuMzUgMTcuMDkgMTk2LjA1IDE2LjU0UTE5NS43NSAxNiAxOTUuMjQgMTUuNzBRMTk0LjcyIDE1LjQwIDE5NC4wOCAxNS40MEwxOTQuMDggMTUuNDBRMTkzLjQ1IDE1LjQwIDE5Mi45MyAxNS43MFExOTIuNDIgMTYgMTkyLjEyIDE2LjU0UTE5MS44MiAxNy4wOSAxOTEuODIgMTcuODBaTTIwNi43MiAxOS40NkwyMDMuMjIgMTkuNDZMMjAzLjIyIDE3LjcxTDIwNi43MiAxNy43MUwyMDYuNzIgMTkuNDZaTTIxNC4wMCAyMkwyMTEuNjIgMjJMMjExLjYyIDEzLjYwTDIxNS40NiAxMy42MFEyMTYuNjEgMTMuNjAgMjE3LjQ1IDEzLjk4UTIxOC4yOCAxNC4zNSAyMTguNzQgMTUuMDZRMjE5LjIwIDE1Ljc2IDIxOS4yMCAxNi43MUwyMTkuMjAgMTYuNzFRMjE5LjIwIDE3LjYyIDIxOC43NyAxOC4zMFEyMTguMzQgMTguOTggMjE3LjU1IDE5LjM2TDIxNy41NSAxOS4zNkwyMTkuMzYgMjJMMjE2LjgyIDIyTDIxNS4yOSAxOS43N0wyMTQuMDAgMTkuNzdMMjE0LjAwIDIyWk0yMTQuMDAgMTUuNDdMMjE0LjAwIDE3LjkzTDIxNS4zMiAxNy45M1EyMTYuMDUgMTcuOTMgMjE2LjQyIDE3LjYxUTIxNi43OSAxNy4yOSAyMTYuNzkgMTYuNzFMMjE2Ljc5IDE2LjcxUTIxNi43OSAxNi4xMiAyMTYuNDIgMTUuNzlRMjE2LjA1IDE1LjQ3IDIxNS4zMiAxNS40N0wyMTUuMzIgMTUuNDdMMjE0LjAwIDE1LjQ3Wk0yMzAuNzMgMjJMMjIzLjk4IDIyTDIyMy45OCAxMy42MEwyMzAuNTggMTMuNjBMMjMwLjU4IDE1LjQ0TDIyNi4zNCAxNS40NEwyMjYuMzQgMTYuODVMMjMwLjA3IDE2Ljg1TDIzMC4wNyAxOC42M0wyMjYuMzQgMTguNjNMMjI2LjM0IDIwLjE3TDIzMC43MyAyMC4xN0wyMzAuNzMgMjJaTTIzNC45NSAyMS4yNEwyMzQuOTUgMjEuMjRMMjM1LjczIDE5LjQ5UTIzNi4yOSAxOS44NiAyMzcuMDMgMjAuMDlRMjM3Ljc4IDIwLjMyIDIzOC41MCAyMC4zMkwyMzguNTAgMjAuMzJRMjM5Ljg2IDIwLjMyIDIzOS44NyAxOS42NEwyMzkuODcgMTkuNjRRMjM5Ljg3IDE5LjI4IDIzOS40OCAxOS4xMVEyMzkuMDkgMTguOTMgMjM4LjIyIDE4Ljc0TDIzOC4yMiAxOC43NFEyMzcuMjcgMTguNTMgMjM2LjY0IDE4LjMwUTIzNi4wMCAxOC4wNiAyMzUuNTUgMTcuNTVRMjM1LjA5IDE3LjAzIDIzNS4wOSAxNi4xNkwyMzUuMDkgMTYuMTZRMjM1LjA5IDE1LjM5IDIzNS41MSAxNC43N1EyMzUuOTMgMTQuMTUgMjM2Ljc3IDEzLjc5UTIzNy42MCAxMy40MyAyMzguODEgMTMuNDNMMjM4LjgxIDEzLjQzUTIzOS42MyAxMy40MyAyNDAuNDQgMTMuNjJRMjQxLjI1IDEzLjgwIDI0MS44NiAxNC4xN0wyNDEuODYgMTQuMTdMMjQxLjEzIDE1LjkzUTIzOS45MyAxNS4yOCAyMzguODAgMTUuMjhMMjM4LjgwIDE1LjI4UTIzOC4wOSAxNS4yOCAyMzcuNzcgMTUuNDlRMjM3LjQ0IDE1LjcwIDIzNy40NCAxNi4wNEwyMzcuNDQgMTYuMDRRMjM3LjQ0IDE2LjM3IDIzNy44MyAxNi41NFEyMzguMjEgMTYuNzEgMjM5LjA2IDE2Ljg5TDIzOS4wNiAxNi44OVEyNDAuMDIgMTcuMTAgMjQwLjY1IDE3LjMzUTI0MS4yOCAxNy41NiAyNDEuNzQgMTguMDdRMjQyLjIxIDE4LjU4IDI0Mi4yMSAxOS40NkwyNDIuMjEgMTkuNDZRMjQyLjIxIDIwLjIxIDI0MS43OSAyMC44M1EyNDEuMzcgMjEuNDQgMjQwLjUzIDIxLjgwUTIzOS42OSAyMi4xNyAyMzguNDkgMjIuMTdMMjM4LjQ5IDIyLjE3UTIzNy40NyAyMi4xNyAyMzYuNTEgMjEuOTJRMjM1LjU0IDIxLjY3IDIzNC45NSAyMS4yNFpNMjQ4LjU4IDE1LjQ4TDI0NS45OSAxNS40OEwyNDUuOTkgMTMuNjBMMjUzLjUyIDEzLjYwTDI1My41MiAxNS40OEwyNTAuOTUgMTUuNDhMMjUwLjk1IDIyTDI0OC41OCAyMkwyNDguNTggMTUuNDhaTTI2MS4xMyAxOS40NkwyNTcuNjIgMTkuNDZMMjU3LjYyIDE3LjcxTDI2MS4xMyAxNy43MUwyNjEuMTMgMTkuNDZaTTI2OC40MCAyMkwyNjYuMDMgMjJMMjY2LjAzIDEzLjYwTDI3Mi42MiAxMy42MEwyNzIuNjIgMTUuNDRMMjY4LjQwIDE1LjQ0TDI2OC40MCAxNy4yOEwyNzIuMTEgMTcuMjhMMjcyLjExIDE5LjEyTDI2OC40MCAxOS4xMkwyNjguNDAgMjJaTTI3OS41OSAyMkwyNzcuMjEgMjJMMjc3LjIxIDEzLjYwTDI4MS4wNSAxMy42MFEyODIuMjAgMTMuNjAgMjgzLjA0IDEzLjk4UTI4My44NyAxNC4zNSAyODQuMzMgMTUuMDZRMjg0Ljc5IDE1Ljc2IDI4NC43OSAxNi43MUwyODQuNzkgMTYuNzFRMjg0Ljc5IDE3LjYyIDI4NC4zNiAxOC4zMFEyODMuOTMgMTguOTggMjgzLjE0IDE5LjM2TDI4My4xNCAxOS4zNkwyODQuOTUgMjJMMjgyLjQxIDIyTDI4MC44OCAxOS43N0wyNzkuNTkgMTkuNzdMMjc5LjU5IDIyWk0yNzkuNTkgMTUuNDdMMjc5LjU5IDE3LjkzTDI4MC45MSAxNy45M1EyODEuNjQgMTcuOTMgMjgyLjAxIDE3LjYxUTI4Mi4zOCAxNy4yOSAyODIuMzggMTYuNzFMMjgyLjM4IDE2LjcxUTI4Mi4zOCAxNi4xMiAyODIuMDEgMTUuNzlRMjgxLjY0IDE1LjQ3IDI4MC45MSAxNS40N0wyODAuOTEgMTUuNDdMMjc5LjU5IDE1LjQ3Wk0yOTAuOTkgMjJMMjg4LjU3IDIyTDI5Mi4yOCAxMy42MEwyOTQuNjIgMTMuNjBMMjk4LjMzIDIyTDI5NS44NyAyMkwyOTUuMjAgMjAuMzdMMjkxLjY1IDIwLjM3TDI5MC45OSAyMlpNMjkzLjQzIDE1LjkzTDI5Mi4zNSAxOC42MUwyOTQuNTEgMTguNjFMMjkzLjQzIDE1LjkzWk0zMDQuNjkgMjJMMzAyLjQ5IDIyTDMwMi40OSAxMy42MEwzMDQuNDUgMTMuNjBMMzA3LjQwIDE4LjQ1TDMxMC4yOCAxMy42MEwzMTIuMjMgMTMuNjBMMzEyLjI2IDIyTDMxMC4wOCAyMkwzMTAuMDUgMTcuNTVMMzA3Ljg5IDIxLjE3TDMwNi44NCAyMS4xN0wzMDQuNjkgMTcuNjdMMzA0LjY5IDIyWk0zMjQuMTYgMjJMMzE3LjQyIDIyTDMxNy40MiAxMy42MEwzMjQuMDEgMTMuNjBMMzI0LjAxIDE1LjQ0TDMxOS43NyAxNS40NEwzMTkuNzcgMTYuODVMMzIzLjUxIDE2Ljg1TDMyMy41MSAxOC42M0wzMTkuNzcgMTguNjNMMzE5Ljc3IDIwLjE3TDMyNC4xNiAyMC4xN0wzMjQuMTYgMjJaTTMzMS4wNSAyMkwzMjguMzIgMTMuNjBMMzMwLjc3IDEzLjYwTDMzMi40NiAxOC45NkwzMzQuMjMgMTMuNjBMMzM2LjQyIDEzLjYwTDMzOC4xMSAxOS4wMUwzMzkuODggMTMuNjBMMzQyLjE0IDEzLjYwTDMzOS40MiAyMkwzMzYuODggMjJMMzM1LjI3IDE2Ljg5TDMzMy41OSAyMkwzMzEuMDUgMjJaTTM0Ni4yMyAxNy44MEwzNDYuMjMgMTcuODBRMzQ2LjIzIDE2LjU1IDM0Ni44MyAxNS41NVEzNDcuNDQgMTQuNTYgMzQ4LjUwIDE0LjAwUTM0OS41NiAxMy40MyAzNTAuODkgMTMuNDNMMzUwLjg5IDEzLjQzUTM1Mi4yMiAxMy40MyAzNTMuMjkgMTQuMDBRMzU0LjM1IDE0LjU2IDM1NC45NiAxNS41NVEzNTUuNTYgMTYuNTUgMzU1LjU2IDE3LjgwTDM1NS41NiAxNy44MFEzNTUuNTYgMTkuMDUgMzU0Ljk2IDIwLjA0UTM1NC4zNSAyMS4wNCAzNTMuMjkgMjEuNjBRMzUyLjIzIDIyLjE3IDM1MC44OSAyMi4xN0wzNTAuODkgMjIuMTdRMzQ5LjU2IDIyLjE3IDM0OC41MCAyMS42MFEzNDcuNDQgMjEuMDQgMzQ2LjgzIDIwLjA0UTM0Ni4yMyAxOS4wNSAzNDYuMjMgMTcuODBaTTM0OC42MiAxNy44MEwzNDguNjIgMTcuODBRMzQ4LjYyIDE4LjUxIDM0OC45MyAxOS4wNVEzNDkuMjMgMTkuNjAgMzQ5Ljc0IDE5LjkwUTM1MC4yNiAyMC4yMCAzNTAuODkgMjAuMjBMMzUwLjg5IDIwLjIwUTM1MS41MyAyMC4yMCAzNTIuMDUgMTkuOTBRMzUyLjU2IDE5LjYwIDM1Mi44NiAxOS4wNVEzNTMuMTYgMTguNTEgMzUzLjE2IDE3LjgwTDM1My4xNiAxNy44MFEzNTMuMTYgMTcuMDkgMzUyLjg2IDE2LjU0UTM1Mi41NiAxNiAzNTIuMDUgMTUuNzBRMzUxLjUzIDE1LjQwIDM1MC44OSAxNS40MEwzNTAuODkgMTUuNDBRMzUwLjI1IDE1LjQwIDM0OS43NCAxNS43MFEzNDkuMjMgMTYgMzQ4LjkzIDE2LjU0UTM0OC42MiAxNy4wOSAzNDguNjIgMTcuODBaTTM2Mi42NyAyMkwzNjAuMjkgMjJMMzYwLjI5IDEzLjYwTDM2NC4xMyAxMy42MFEzNjUuMjggMTMuNjAgMzY2LjEyIDEzLjk4UTM2Ni45NSAxNC4zNSAzNjcuNDEgMTUuMDZRMzY3Ljg3IDE1Ljc2IDM2Ny44NyAxNi43MUwzNjcuODcgMTYuNzFRMzY3Ljg3IDE3LjYyIDM2Ny40NCAxOC4zMFEzNjcuMDEgMTguOTggMzY2LjIyIDE5LjM2TDM2Ni4yMiAxOS4zNkwzNjguMDMgMjJMMzY1LjQ5IDIyTDM2My45NiAxOS43N0wzNjIuNjcgMTkuNzdMMzYyLjY3IDIyWk0zNjIuNjcgMTUuNDdMMzYyLjY3IDE3LjkzTDM2My45OSAxNy45M1EzNjQuNzIgMTcuOTMgMzY1LjA5IDE3LjYxUTM2NS40NiAxNy4yOSAzNjUuNDYgMTYuNzFMMzY1LjQ2IDE2LjcxUTM2NS40NiAxNi4xMiAzNjUuMDkgMTUuNzlRMzY0LjcyIDE1LjQ3IDM2My45OSAxNS40N0wzNjMuOTkgMTUuNDdMMzYyLjY3IDE1LjQ3Wk0zNzUuMDEgMjJMMzcyLjY1IDIyTDM3Mi42NSAxMy42MEwzNzUuMDEgMTMuNjBMMzc1LjAxIDE3LjA5TDM3OC4yNiAxMy42MEwzODAuODcgMTMuNjBMMzc3LjQ1IDE3LjMyTDM4MS4wNiAyMkwzNzguMzAgMjJMMzc1Ljg5IDE4Ljk1TDM3NS4wMSAxOS45MEwzNzUuMDEgMjJaIiBmaWxsPSIjRkZGRkZGIiB4PSIxMjYuMzEiLz48L3N2Zz4=)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![Flake8 Status](./reports/flake8/flake8-badge.svg?dummy=8484744)](reports/flake8/index.html)

Une application de gestion de la relation client (CRM), qui effectue le suivi de tous les clients et événements :
* L'application permettra essentiellement à l'equipe de suivre des clients, de leur ajouter des contracts, associés à des événements.
* L'applications exploitera **les points de terminaison d'API qui serviront les données**, ou le site d'admin de django.
* Principales fonctionnalités de l'application (autre que celle :
  - Authentification JWT des utilisateurs.
  - Permissions;Il est interdit à tout utilisateur autorisé autre que les membres de l'équipe associé au contrat et événements, d'émettre des requêtes d'actualisation.
  - L'équipe des gestionnaires sont les seuls capable à pouvoir supprimer, via le site d'admin de django.
  - respecte les normes OWASP et RGPD. 


### Prérequis
* [Python v3.x+](https://www.python.org/downloads/) .
* [PostGreSql](https://www.postgresql.org/download/). (configuration voir ci-dessous)
* Git installé (conseillé)

# INSTALLATION ( pour windows )


Créer un dossier vide. Il contiendra le code complet du projet
## *1. Installation du site*

Ouvrez un terminal:

Depuis le dossier précédemment créé, clonez le repository du programme avec la commande :

<pre><code>git clone https://github.com/Nathom78/Developpez_une_architecture_back-end_securisee_en_utilisant_Django_ORM.git</code></pre>

Ou utiliser [ce repository](https://github.com/Nathom78/Developpez_une_architecture_back-end_securisee_en_utilisant_Django_ORM.git) en téléchargeant le zip.
<br>


## *2. Installer un environnement python*

D'abord créer à partir de la racine du projet un environnement, ici appellé ".env"

`PS D:\..\> python -m venv .env`

Ensuite activer l'environnement python: 

`PS D:\..\> .env\Scripts\activate.ps1`


## *3. Installer les paquets nécessaires aux projets.*

<br>
Taper la commande suivante : 
<pre><code>
pip install -r requirements.txt
</code></pre>

Pour vérifier, taper cette commande :
<pre><code>pip list</code></pre>
Et vous devriez avoir :
<pre><code>Package                       Version
----------------------------- --------
asgiref                       3.7.2
attrs                         23.1.0
certifi                       2023.5.7
charset-normalizer            3.2.0
click                         8.1.6
colorama                      0.4.6
Django                        4.2.3
djangorestframework           3.14.0
djangorestframework-simplejwt 5.2.2
drf-spectacular               0.26.4
idna                          3.4
inflection                    0.5.1
Jinja2                        3.1.2
jsonschema                    4.18.4
jsonschema-specifications     2023.7.1
MarkupSafe                    2.1.3
mccabe                        0.7.0
Pillow                        10.0.0
pip                           23.2.1
psycopg                       3.1.9
psycopg-binary                3.1.9
pycodestyle                   2.10.0
pyflakes                      3.0.1
Pygments                      2.15.1
PyJWT                         2.8.0
pyrsistent                    0.19.3
pytz                          2023.3
PyYAML                        6.0
referencing                   0.30.0
requests                      2.31.0
rpds-py                       0.8.10
sentry-sdk                    1.28.1
setuptools                    68.0.0
sqlparse                      0.4.4
typing_extensions             4.7.1
tzdata                        2023.3
uritemplate                   4.1.1
urllib3                       2.0.3
wheel                         0.38.4
</code></pre>
## *4. configuration PostGreSql*
Utiliser les variables environments afin d'indiquer le chemin : (sinon utiliser les chemins par default)
- PGSERVICEFILE pour le fichier [.pg_service.conf](https://www.postgresql.org/docs/current/libpq-pgservice.html)
<pre><code>[My_db]
host=localhost
user=ThomasEpic
dbname=Epic
port=5432
</code></pre>
- PGPASSFILE pour le fichier [pgpass.conf](https://www.postgresql.org/docs/current/libpq-pgpass.html)
<pre><code>localhost:5432:Epic:ThomasEpic:ThomasAdmin</code></pre>

En Ayant par exemple [pgAdmin 4](https://www.pgadmin.org/download/) d'installé par ce lien, si la version installé par EDB ne fonctionne pas : 

Avec une base de donné crée comme *Epic*, en plus de celle de base *postgres*.

Avec un user avec les priviléges minimum ici *ThomasEpic* et son mot de passe *ThomasAdmin*.
## *5. Execution du logiciel*

Dans une fenêtre de terminal, se placer à la racine de l'application
ici Epic, ensuite taper les commandes suivantes :

Tout d'abord, nous devons appliquer les migrations à la base de donnée,
afin de pouvoir utiliser dans ce nouvel environnement, la base PostGreSql crée. 
<pre><code>
(.env) PS ~...\Epic> py manage.py migrate
</code></pre>

Ensuite, nous pouvons lancer l'application à travers le serveur Django.

<pre><code>
(.env) PS ~...\Epic py manage.py runserver 
</code></pre>

## *6. Urls avec drf-spectacular package*
### documentations de l'API
This exposes 3 endpoints:
- A YAML view of your API specification at /crm/schema/
- A swagger-ui view of your API specification at /crm/schema/swagger-ui/
- A ReDoc view of your API specification at /crm/schema/redoc/


## *7. Documentation Postman publique*
https://documenter.getpostman.com/view/21242674/2s9XxsVc52
***
# Technologies
<p>
<img src="https://skillicons.dev/icons?i=git,github,python,django,postgresql,postman&theme=dark">
</p>

![logo](https://www.django-rest-framework.org/img/logo.png)

***
## *Conventions de nommage et de codes :*
<p>PEP 8 – Style Guide for Python Code
<a href="https://peps.python.org/pep-0008/">ici</a>.
</p>

Un rapport **flake8** au format HTML est disponible dans le repertoire `\flake-report`, à la racine du projet.


