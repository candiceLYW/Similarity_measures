SELECT lc.user_id as user_id, books.id as book_id, 1 as rating
FROM library_cards AS lc
INNER JOIN documents
ON lc.document_id = documents.id
INNER JOIN books
ON documents.book_id = books.id
WHERE lc.state != 'removed'
-- Исключаем приватные книги 0b010101 == 21
-- AND NOT (books.flags & 21)
-- Исключаяем из выборки tinybirdNN-пользователей
AND lc.user_id NOT BETWEEN 928984 AND 929113
-- Исключаяем из выборки книги, который добавляются пользователю автоматически
AND documents.uuid
NOT IN (
  'GhNU51oG',
  'G7m9lpw5',
  'FHE14xQr',
  'Yewrdh75',
  'jBaBabTB',
  'sVQbYafk',
  'xnNBkIcV',
  'XLsFM9Q5',
  'w5gC9Y8N',
  'BDXwOSjN',
  'cChh5JAt',
  'wsyA9erN'
);
