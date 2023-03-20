import lexer


# Test le lexer sous différentes conditions,
def test_lexer():
    # 1 - Valid PGN
    ret = test_valid_pgn_1()
    if not ret:
        print("\033[92m [PASS] - Fichier valide avec une partie ")
    else:
        print("\033[91m [FAIL] - Fichier valide avec une partie, err " + ret)
    ret = test_valid_pgn_2()
    if not ret:
        print("\033[92m [PASS] - Fichier valide avec une partie ")
    else:
        print("\033[91m [FAIL] - Fichier valide avec une partie, err " + ret)
    ret = test_valid_pgn_3()
    if not ret:
        print("\033[92m [PASS] - Fichier valide avec deux partie ")
    else:
        print("\033[91m [FAIL] - Fichier valide avec deux partie, err ")
        for re in ret:
            print(re + " - ")
    ret = test_valid_pgn_4()
    if not ret:
        print("\033[92m [PASS] - Fichier valide avec une partie ")
    else:
        print("\033[91m [FAIL] - Fichier valide avec une, err ")
        for re in ret:
            print(re + " - ")


def test_valid_pgn_1():
    pgn = '[Event "Mannheim"] ' \
          '[Site "Mannheim GER"]' \
          '[Date "1914.08.01"]' \
          '[EventDate "1914.07.20"]' \
          '[Round "11"]' \
          '[Result "1-0"]' \
          '[White "Alexander Alekhine"]' \
          '[Black "Hans Fahrni"]' \
          '[ECO "C13"]' \
          '[WhiteElo "?"]' \
          '[BlackElo "?"]' \
          '[PlyCount "45"]' \
          '1. e4 {Notes by Richard Reti} 1... e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 ' \
          '6. h4 {This ingenious method of play which has subsequently been adopted by all' \
          'modern masters is characteristic of Alekhine s style.} 6... Bxg5 7. hxg5 Qxg5 ' \
          '8. Nh3 {! The short-stepping knight is always brought as near as possible to' \
          'the actual battle field. Therefore White does not make the plausible move 8 Nf3' \
          'but 8 Nh3 so as to get the knight to f4.} 8... Qe7 9. Nf4 Nf8 10. Qg4 f5 {The' \
          'only move. Not only was 11 Qxg7 threatened but also Nxd5.} 11. exf6 gxf6 12. ' \
          'O-O-O {He again threatens Nxd5.} 12... c6 13. Re1 Kd8 14. Rh6 e5 15. Qh4 Nbd7 ' \
          '16. Bd3 e4 17. Qg3 Qf7 {Forced - the sacrifice of the knight at d5 was' \
          'threatened and after 17...Qd6 18 Bxe4 dxe4 19 Rxe4 and 20 Qg7 wins.} 18. Bxe4 ' \
          'dxe4 19. Nxe4 Rg8 20. Qa3 {Here, as so often happens, a surprising move and one' \
          'difficult to have foreseen, forms the kernel of an apparently simple Alekhine' \
          'combination.} 20... Qg7 {After 20.Qe7 21.Qa5+ b6 22.Qc3 would follow.} 21. ' \
          'Nd6 Nb6 22. Ne8 Qf7 {White mates in three moves.} 23. Qd6+ 1-0'
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgn)
    return lex.error


def test_valid_pgn_2():
    pgn = "1. e4 e5 2... Nf3 { Nh3 it's considered bad } 2... Nc6 1/2-1/2"
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgn)
    return lex.error


def test_valid_pgn_3():
    pgn = '[Event "F/S Return Match"]' \
          '[Site "Belgrade, Serbia JUG"]' \
          '[Date "1992.11.04"]' \
          '[Round "29"]' \
          '[White "Fischer, Robert J."]' \
          '[Black "Spassky, Boris V."]' \
          '[Result "1/2-1/2"]' \
          '1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 ' \
          'O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15. ' \
          'Nb1 h6 16. Bh4 c5 17. dxe5 Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. ' \
          'Nc4 Nxc4 22. Bxc4 Nb6 23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7 ' \
          '27. Qe3 Qg5 28. Qxg5 hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33. ' \
          'f3 Bc8 34. Kf2 Bf5 35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5 ' \
          '40. Rd6 Kc5 41. Ra6 Nf2 42. g4 Bd3 43. Re6 1/2-1/2'
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgn)
    return lex.error


def test_valid_pgn_4():
    pgn = """
    [Event "F/S Return Match"]
    [Site "Belgrade Serbia JUG"]
    [Date "1992.11 04"]
    [Round "29"]
    [White "Fischer, Robert J."]
    [Black "Spassky, Boris V."]
    [Result "1/2 1/2"]

    1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3
    O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15.
    Nb1 h6 16. Bh4 c5 17. dxe5 Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21.
    Nc4 Nxc4 22. Bxc4 Nb6 23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7
    27. Qe3 Qg5 28. Qxg5 hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33.
    f3 Bc8 34. Kf2 Bf5 35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5
    40. Rd6 Kc5 41. Ra6 Nf2 42. g4 Bd3 43. Re6 1/2-1/2
    """
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgn)
    return lex.error
